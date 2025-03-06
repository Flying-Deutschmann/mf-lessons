# **SSH into the EC2 Instance**

Once the instance is created, follow these steps to SSH into the EC2 instance.

### **1. Obtain the Public IP Address of Your Instance**:

When you built your EC2 instance, you should have had a public IP printed

### **2. SSH into the Instance**
#### **For Linux or macOS Users**:

1. Open a terminal (Git Bash).
2. Use the following SSH command, replacing `<path-to-your-key-pair.pem>` with the actual path to your private key file, and `<Public-IP>` with the public IP or DNS name of your EC2 instance.

   ```bash
   ssh -i /path/to/your-key-pair.pem ec2-user@<Public-IP>
   ```

   **Example**:
   ```bash
   ssh -i ~/my-aws-keys/my-key.pem ec2-user@54.123.45.67
   ```

3. **Ensure your private key file is secure** by setting its permissions to `400` (if you're on Linux/Mac):
   ```bash
   chmod 400 /path/to/your-key-pair.pem
   ```

4. You should now be logged into the EC2 instance. You can run commands and interact with your instance.

---

## **Step 3: Troubleshooting SSH Access**

1. **Security Group Configuration**:
   - Make sure the **Security Group** associated with your EC2 instance has an **Inbound Rule** allowing **SSH (port 22)** from your IP.
   - You can check or add the rule in the **Security Groups** section of the **EC2 Console**.

     Example:
     - Type: `SSH`
     - Protocol: `TCP`
     - Port: `22`
     - Source: `Your IP` (or `0.0.0.0/0` for all IPs, but this is less secure).

2. **Correct Username**:
   - Make sure you are using the correct username for your EC2 instance based on the AMI:
     - **Amazon Linux 2 AMI**: `ec2-user`
     - **Ubuntu AMI**: `ubuntu`
     - **RHEL AMI**: `ec2-user`
     - **CentOS AMI**: `centos`

3. **Key Pair Mismatch**:
   - Ensure you are using the **correct private key** file (`.pem` or `.ppk`) that corresponds to the key pair used during instance creation.

4. **Instance State**:
   - Ensure that your EC2 instance is in the **running** state and not stopped or terminated.

---

## **Conclusion**

You have now successfully created an EC2 instance using Boto3 and SSH'd into it. You can use this instance for development, testing, or any other use case you have in mind.
