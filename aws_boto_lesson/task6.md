# **Create an S3 Bucket and Upload Then Download File Using Boto3**
This guide explains how to create an **S3 bucket** and upload a file to it using **Boto3**, the AWS SDK for Python. Follow the steps below to interact with AWS S3 and perform these actions programmatically.

---

## **Prerequisites**
Before you start, ensure you have the Virtal Environment for python setup and activated.
Ensure you have AWS credential file created and setup.
- Firefox browser
- Python3.10+
- Boto3

```bash
Firefox instruction_setup_venv.md
```

### **Create a local file**
You will require a local file to be created and pushed to the S3 bucket first.
```bash
echo "This is an s3 test" >> local_file.txt
```

## **Step 1: Python Script to Create an S3 Bucket and Upload and Download File**

### **Python Script: `s3_operations.py`**

```python
import boto3

# Initialize the S3 client
s3 = boto3.client('s3')

# 1. Create a new S3 bucket
response = s3.create_bucket(Bucket='my-new-bucket')

# Print response for debugging purposes
print("Bucket Creation Response:", response)

# 2. Upload a local file to the S3 bucket
s3.upload_file('local_file.txt', 'my-new-bucket', 'uploaded_file.txt')

# Print confirmation message after successful upload
print("File uploaded successfully!")

# 3. Download a file from the S3 bucket to local system
s3.download_file('my-new-bucket', 'uploaded_file.txt', 'downloaded_file.txt')

# Print confirmation message after successful download
print("File downloaded successfully!")
```

### **Explanation**:
- **`boto3.client('s3')`**: Initializes an S3 client that allows you to interact with S3 services.
- **`create_bucket(Bucket='my-new-bucket')`**: Creates an S3 bucket named `my-new-bucket`. You can change the bucket name to any unique name.
- **`upload_file('local_file.txt', 'my-new-bucket', 'uploaded_file.txt')`**: Uploads a file named `local_file.txt` from your local system to the `my-new-bucket` S3 bucket, and the file is stored as `uploaded_file.txt`.
- ** `download_file('my-new-bucket', 'uploaded_file.txt', 'downloaded_file.txt')`**: Downloads the file uploaded_file.txt from the my-new-bucket S3 bucket to your local system as downloaded_file.txt.

---

## **Step 2: Run the Python Script**

1. Save the script as `s3_operations.py`.
2. Open your terminal or command prompt and navigate to the directory where you saved the script.
3. Run the script:
   ```bash
   python s3_operations.py
   ```

4. If successful, you should see the following output:

   ```
   Bucket Creation Response: {'Location': '/my-new-bucket'}
   File uploaded successfully!
   ```

---

## **Step 3: Verify the Bucket and Uploaded File**

1. **Go to the S3 Console**:
   - Navigate to the [AWS S3 Console](https://s3.console.aws.amazon.com/s3/home).
   - You should see the `my-new-bucket` listed under your buckets.

2. **Check the uploaded file**:
   - Inside the `my-new-bucket`, you should see the `uploaded_file.txt` file that was uploaded from your local system.

## **Conclusion**

You’ve successfully created an S3 bucket and uploaded a file to it using **Boto3** in Python!  explanations are designed to be easy to follow, helping you interact with AWS S3 programmatically.
