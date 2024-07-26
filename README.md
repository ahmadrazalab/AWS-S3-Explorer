# s3-web-ui-tool

## Why this tool / How to use it
This tool is designed to navigate in the S3 bucket using a web browser. It requires access keys and secret keys to get access to the S3 bucket. You can navigate through each file and folder inside the S3 bucket. 

This tool can also be used to open any files in the S3 bucket (the bucket can be private). When you click on any file, it will open the file in the browser using a presigned URL which is valid for 1 hour.

## Features
- Browse and navigate S3 bucket contents
- Open files in the S3 bucket
- Supports private buckets
- Presigned URL generation for secure file access (1-hour validity)

## Installation
1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project folder:
    ```bash
    cd <folder>
    ```

3. Install dependencies (if any). Ensure you have Python3 and necessary libraries installed.

## Run Application
To start the application, run the following command:
```bash
pip install -r requirements.txt
python3 app.py
```

## Requirements
- Python 3.x
- AWS access keys with S3 permissions

## Configuration
Ensure your AWS access keys and secret keys are configured properly for the tool to access your S3 bucket.
