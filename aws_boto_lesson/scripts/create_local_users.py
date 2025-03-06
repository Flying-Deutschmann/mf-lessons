import boto3
import pywinrm
from getpass import getpass

# Initialize the IAM client
iam = boto3.client('iam')

# Example users with their respective IP addresses
users = [
    {"username": "user1", "ip": "192.168.0.188"},
    {"username": "user2", "ip": "192.168.0.48"},
    {"username": "user3", "ip": "192.168.0.109"},
    {"username": "user4", "ip": "192.168.0.128"}
]

# Define the custom policy
policy_name = "S3_EC2_Create_Policy"
policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:CreateBucket",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::*",
                "arn:aws:s3:::*/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:RunInstances",
                "ec2:DescribeInstances",
                "ec2:DescribeImages",
                "ec2:DescribeKeyPairs",
                "ec2:DescribeSecurityGroups"
            ],
            "Resource": "*"
        }
    ]
}

# Function to create IAM user and keys
def create_user(username):
    try:
        response = iam.create_user(UserName=username)
        print(f"User {username} created successfully.")
        
        # Create access key
        create_access_key_response = iam.create_access_key(UserName=username)
        access_key_id = create_access_key_response['AccessKey']['AccessKeyId']
        secret_access_key = create_access_key_response['AccessKey']['SecretAccessKey']

        print(f"Access Key ID: {access_key_id}")
        print(f"Secret Access Key: {secret_access_key}")

        return access_key_id, secret_access_key

    except Exception as e:
        print(f"Error creating user {username}: {e}")
    return None, None

# Function to create the policy
def create_policy():
    try:
        create_policy_response = iam.create_policy(
            PolicyName=policy_name,
            PolicyDocument=str(policy_document).replace("'", "\"")
        )
        print(f"Policy created with ARN: {create_policy_response['Policy']['Arn']}")
        return create_policy_response['Policy']['Arn']
    except iam.exceptions.EntityAlreadyExistsException:
        print(f"Policy {policy_name} already exists.")
        return f"arn:aws:iam::aws:policy/{policy_name}"

# Function to attach policy to users
def attach_policy_to_users(policy_arn):
    for user_info in users:
        try:
            iam.attach_user_policy(
                UserName=user_info['username'],
                PolicyArn=policy_arn
            )
            print(f"Policy attached to {user_info['username']}")
        except Exception as e:
            print(f"Error attaching policy to {user_info['username']}: {e}")

# Function to push AWS credentials to remote Windows machine
def push_credentials_to_windows(remote_ip, username, access_key_id, secret_access_key):
    # Define the PowerShell script to set AWS credentials on Windows
    ps_script = f"""
    $AccessKeyId = "{access_key_id}"
    $SecretAccessKey = "{secret_access_key}"
    $AwsCredsPath = "$env:USERPROFILE\\.aws\\credentials"
    Set-Content -Path $AwsCredsPath -Value "[default]`naws_access_key_id=$AccessKeyId`naws_secret_access_key=$SecretAccessKey"
    """

    try:
        # Connect to the Windows machine using WinRM
        session = pywinrm.Session(
            f'http://{remote_ip}:5985/wsman',
            auth=(username, getpass(f"Enter password for {username}@{remote_ip}: ")),
            transport='ntlm'
        )

        # Run the PowerShell script remotely
        result = session.run_ps(ps_script)
        print(f"Successfully pushed credentials to {remote_ip}: {result.std_out.decode()}")
    except Exception as e:
        print(f"Error pushing credentials to {remote_ip}: {e}")

if __name__ == '__main__':
    # Create the policy and get its ARN
    policy_arn = create_policy()

    # Loop through users, create them, generate keys and push them to Windows machines
    for user_info in users:
        access_key_id, secret_access_key = create_user(user_info["username"])

        if access_key_id and secret_access_key:
            # Push the keys to the user's Windows machine using the specific IP
            push_credentials_to_windows(user_info['ip'], user_info["username"], access_key_id, secret_access_key)

    # Attach the policy to each user
    attach_policy_to_users(policy_arn)
    print("Users created, access keys pushed to machines, and policy attached.")
