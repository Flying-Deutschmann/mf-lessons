# **Setting up Python Virtal Environment and Dependancies**

1. **AWS Account**: You must have an active AWS account. If you don't have one, you can [sign up for AWS](https://aws.amazon.com).
2. **AWS CLI**: Install and configure the AWS CLI to interact with your AWS resources through Boto3.

   Enable the Python Environment
   ```bash
   python -m venv venv
   source venv/Scripts/activate
   ```

   To install AWS CLI:
   ```bash
   pip install awscli
   ```

   Then, configure it:
   ```bash
   aws configure
   ```

   You will need to input your **Access Key ID**, **Secret Access Key**, **Default Region Name**, and **Default Output Format**.
   
3. **Boto3**: Install the Boto3 library which will allow Python to interact with AWS.

   To install Boto3:
   ```bash
   pip install boto3
   ```
