# **EC2 Instance Creation and SSH Access with Boto3**

This guide walks you through creating an **EC2 instance** using **Boto3**, the AWS SDK for Python, and then SSHing into that instance. It covers all the necessary steps, from launching the EC2 instance to connecting to it via SSH.

---

## **Prerequisites**
Before you start, ensure you have the Virtal Environment for python setup and activated:
- Firefox browser
- Python3.10+
- Boto3

```bash
Firefox instruction_setup_venv.md
```

2. **Key Pair**: You need an **EC2 key pair** (a `.pem` file) to SSH into the instance. You can create it during instance creation, or use an existing one.

3. **SSH Client**:
   - **Linux/Mac**: You can use the built-in terminal.
   - **Windows-GitBash**: You can use the built-in terminal
   - **Windows-PuTTY**: Install **PuTTY** if you’re using Windows (and convert the `.pem` file to `.ppk` format using PuTTYgen).

---

## **Step 1: Python Script to Create an EC2 Instance**

This script uses **Boto3** to launch an EC2 instance with a specified **AMI ID**, **instance type**, and **key pair name**.

### **Python Script: `create_ec2_instance.py`**

```python
import boto3

# Initialize a session using Boto3 EC2 resource
ec2 = boto3.resource('ec2')

# Create a new EC2 instance
instance = ec2.create_instances(
    ImageId='ami-12345678',  # Replace with a valid AMI ID (e.g., Amazon Linux 2 AMI)
    MinCount=1,              # Minimum number of instances to launch
    MaxCount=1,              # Maximum number of instances to launch
    InstanceType='t2.micro', # Type of the instance (t2.micro is eligible for the free tier)
    KeyName='your-key-pair'  # Replace with your SSH key pair name
)

# Print the ID of the created instance
print("Created instance:", instance[0].id)

# Retrieve the public IP address
public_ip = instance.public_ip_address

# Print the public IP address
print("Public IP address of the EC2 instance:", public_ip)
```

### **Explanation**:
- `ImageId`: Specify the AMI ID to use for the instance. For Amazon Linux 2, you can find the ID by searching for Amazon Linux 2 in the AWS EC2 AMI list.
- `MinCount` and `MaxCount`: These are set to `1`, meaning we want to create a single instance.
- `InstanceType`: We're using `t2.micro`, which is eligible for the **AWS Free Tier**.
- `KeyName`: This is the name of the **SSH key pair** that you’ll use to access the instance.

### **Steps to Run the Script**:
1. Save the script as `create_ec2_instance.py`.
2. In your terminal, navigate to the directory where the script is saved.
3. Run the script:
   ```bash
   python create_ec2_instance.py
   ```

4. Once the script runs successfully, it will print the **instance ID** of the newly created EC2 instance.

## **Conclusion**

This script allows you to quickly create EC2 instances on AWS using the Boto3 library. It's an easy way to automate instance creation and interact with your AWS resources programmatically.
