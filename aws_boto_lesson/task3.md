# **How to Set Up AWS Credentials for Boto3 and AWS CLI**

This guide will show you how to create and configure the `~/.aws/credentials` file on your local machine to enable **Boto3** (AWS SDK for Python) and **AWS CLI** to interact with AWS services.

---

## **Prerequisites**
Before you proceed, ensure you have setup the python environment and installed the python dependancies.
```bash
msedge instruction_setup_venv.md
```

**AWS Access Key & Secret Key**: To interact with AWS services programmatically, you need an **Access Key** and a **Secret Key**. These have been added as a text file to your computer `keys.txt`.

---

## **Step 1: Install the AWS CLI (Command Line Interface)**

If you don't have the AWS CLI installed, you need to install it to configure your credentials.

### **For Windows**:
1. Download the latest version of the AWS CLI from the [Windows installation guide](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-windows.html).
2. Follow the installation instructions.

### **For macOS/Linux**:
1. Download and install the AWS CLI using the instructions from the [CLI installation guide](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).

---

## **Step 2: Configure AWS Credentials Using the AWS CLI**

Once you have the AWS CLI installed, you can configure the AWS credentials by running the `aws configure` command.

1. Open your terminal or command prompt.
2. Run the following command to configure your AWS credentials:

   ```bash
   aws configure
   ```

3. You will be prompted to enter the following details:
   - **AWS Access Key ID**: Enter your **Access Key ID** (generated in the AWS IAM console).
   - **AWS Secret Access Key**: Enter your **Secret Access Key**.
   - **Default region name**: Enter the default AWS region you want to work with (e.g., `us-west-2`, `us-east-1`).
   - **Default output format**: Choose an output format (e.g., `json`, `text`, or `table`). You can use `json` as the default.

   Example:
   ```bash
   AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
   AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
   Default region name [None]: us-west-2
   Default output format [None]: json
   ```

   This will create the `~/.aws/credentials` and `~/.aws/config` files in your system.

---

## **Step 3: Manually Editing the `~/.aws/credentials` File (Optional)**

If you'd like to manually edit or verify the credentials, you can open the `~/.aws/credentials` file in a text editor.

### **For Windows**:
- The `credentials` file is typically located at:
  ```
  C:\Users\<YourUsername>\.aws\credentials
  ```

### **For macOS/Linux**:
- The `credentials` file is usually located at:
  ```
  /home/<YourUsername>/.aws/credentials
  ```
  or
  ```
  /Users/<YourUsername>/.aws/credentials
  ```

### **Edit the `credentials` file**:
Open the `credentials` file in a text editor and add your **Access Key ID** and **Secret Access Key**. The format of the file will look like this:

```
[default]
aws_access_key_id = YOUR_ACCESS_KEY_ID
aws_secret_access_key = YOUR_SECRET_ACCESS_KEY
```

For example:

```
[default]
aws_access_key_id = AKIAIOSFODNN7EXAMPLE
aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

You can also add multiple profiles in the same `credentials` file by adding sections with different profile names:

```
[default]
aws_access_key_id = YOUR_ACCESS_KEY_ID
aws_secret_access_key = YOUR_SECRET_ACCESS_KEY

[profile_name]
aws_access_key_id = ANOTHER_ACCESS_KEY_ID
aws_secret_access_key = ANOTHER_SECRET_ACCESS_KEY
```

Replace `profile_name` with a custom profile name that you want to use.

---

## **Step 4: Verify Your Configuration**

You can verify that the `~/.aws/credentials` file is properly configured by running a simple AWS CLI command or using **Boto3** in Python.

### **Verify Using AWS CLI**:
1. Open a terminal or command prompt.
2. Run a simple AWS CLI command, such as listing your S3 buckets:

   ```bash
   aws s3 ls
   ```

   If everything is set up correctly, you should see a list of your S3 buckets.

### **Verify Using Boto3 in Python**:
You can also verify the configuration by running a Boto3 script in Python. Here’s an example to list your S3 buckets:

```python
import boto3

# Initialize the S3 client
s3 = boto3.client('s3')

# List S3 buckets
response = s3.list_buckets()

# Print out the bucket names
print('S3 Buckets:')
for bucket in response['Buckets']:
    print(f'- {bucket["Name"]}')
```

Run the script, and if everything is configured correctly, you should see the names of the S3 test bucket printed.
