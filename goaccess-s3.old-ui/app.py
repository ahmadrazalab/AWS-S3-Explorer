import boto3
import io
import zipfile
from flask import Flask, jsonify, request, send_file

app = Flask(__name__)

# Configuration
S3_BUCKET = "xxxxxxx"
S3_ACCESS_KEY = "xxxxxxx"
S3_SECRET_KEY = "xxxxxxx"
S3_REGION = "xxxxxxx"

# Initialize S3 client
s3_client = boto3.client(
    "s3",
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY,
    region_name=S3_REGION,
)


def list_objects_in_folder(prefix, continuation_token=None):
    """List objects (folders and files) in the specified prefix with pagination."""
    params = {"Bucket": S3_BUCKET, "Prefix": prefix, "Delimiter": "/"}
    if continuation_token:
        params["ContinuationToken"] = continuation_token

    response = s3_client.list_objects_v2(**params)

    folders = [
        {"name": obj.get("Prefix").split("/")[-2], "path": obj.get("Prefix")}
        for obj in response.get("CommonPrefixes", [])
    ]
    files = [
        {"name": obj.get("Key").split("/")[-1], "path": obj.get("Key")}
        for obj in response.get("Contents", [])
    ]

    next_continuation_token = response.get("NextContinuationToken")

    return {
        "folders": folders,
        "files": files,
        "next_continuation_token": next_continuation_token,
    }


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/list-files", methods=["GET"])
def list_files():
    """List root folders in the S3 bucket."""
    try:
        response = list_objects_in_folder("")
        return jsonify(
            {
                "folders": response["folders"],
                "next_continuation_token": response["next_continuation_token"],
            }
        )
    except Exception as e:
        return str(e), 500


@app.route("/list-files-in-folder", methods=["GET"])
def list_files_in_folder():
    """List files in a specific folder in the S3 bucket."""
    try:
        path = request.args.get("path", "")
        response = list_objects_in_folder(path)
        return jsonify({"folders": response["folders"], "files": response["files"]})
    except Exception as e:
        return str(e), 500


@app.route("/generate-url/<path:filename>", methods=["GET"])
def generate_url(filename):
    """Generate a pre-signed URL for the given file."""
    try:
        url = s3_client.generate_presigned_url(
            "get_object", Params={"Bucket": S3_BUCKET, "Key": filename}, ExpiresIn=3600
        )  # URL valid for 1 hour
        return jsonify({"url": url})
    except Exception as e:
        return str(e), 500


@app.route("/download", methods=["GET"])
def download():
    """Download a file or zip folder."""
    path = request.args.get("path", "")
    type = request.args.get("type", "")

    if type == "folder":
        # Zip folder
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zip_file:
            paginator = s3_client.get_paginator("list_objects_v2")
            for page in paginator.paginate(
                Bucket=S3_BUCKET, Prefix=path, Delimiter="/"
            ):
                for obj in page.get("Contents", []):
                    file_key = obj.get("Key")
                    file_name = file_key[len(path) :].lstrip("/")
                    file_obj = s3_client.get_object(Bucket=S3_BUCKET, Key=file_key)
                    zip_file.writestr(file_name, file_obj["Body"].read())
        zip_buffer.seek(0)
        return send_file(
            zip_buffer,
            as_attachment=True,
            download_name=f"{path.rstrip('/').split('/')[-1]}.zip",
            mimetype="application/zip",
        )

    elif type == "file":
        try:
            file_obj = s3_client.get_object(Bucket=S3_BUCKET, Key=path)
            return send_file(
                io.BytesIO(file_obj["Body"].read()),
                as_attachment=True,
                download_name=path.split("/")[-1],
                mimetype="application/octet-stream",
            )
        except Exception as e:
            return str(e), 500


if __name__ == "__main__":
    app.run(debug=True)
