# AWS S3 Navigator

## Why this tool / How to use it
This tool is designed to navigate an S3 bucket using a web browser. It requires access keys and secret keys to access the S3 bucket. You can navigate through each file and folder inside the S3 bucket.

This tool can also be used to open any files in the S3 bucket (the bucket can be private). When you click on any file, it will open the file in the browser using a presigned URL which is valid for 1 hour.

## Features
- Browse and navigate S3 bucket contents
- Open files in the S3 bucket
- Supports private buckets
- Presigned URL generation for secure file access (1-hour validity)
- File search functionality
- File upload capability
- Download files and folders
- Breadcrumb navigation
- Dynamic content display for files and folders

## Installation
1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project folder:
    ```bash
    cd <folder>
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Run Application
To start the application, run the following command:
```bash
python3 app.py
```

## Requirements
- Python 3.x
- AWS access keys with S3 permissions

## Configuration
Ensure your AWS access keys and secret keys are configured properly for the tool to access your S3 bucket.

## Usage
1. Select the desired S3 bucket from the dropdown menu.
2. Use the search bar to find specific files or folders.
3. Navigate through folders by clicking on them.
4. Click on files to open them using a presigned URL.
5. Use the upload section in the header to upload files directly to the selected bucket and current path.
6. Download files or folders using the download button provided.

## Contribution
We welcome contributions from the community. To contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request to the `main` branch.


## Acknowledgements
- Thanks to all contributors and users who have helped improve this project.

> This `README.md` includes all necessary information about the project, including features, installation instructions, usage, contribution guidelines, and licensing. Make sure to replace `<repository-url>` with the actual URL of your repository and include any additional setup or configuration details if necessary.