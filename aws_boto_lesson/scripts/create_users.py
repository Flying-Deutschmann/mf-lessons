import boto3

# Initialize the IAM client
iam = boto3.client('iam')

users = [
    {"username": "user1"},
    {"username": "user2"},
    {"username": "user3"},
    {"username": "user4"},
    {"username": "user5"},
    {"username": "user6"},
    {"username": "user7"},
    {"username": "user8"}
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

def create_user(username):
    try:
        # Create the IAM user
        response = iam.create_user(UserName=username)
        print(f"User {username} created successfully.")
        
        # Optionally, create an access key for the new user
        create_access_key_response = iam.create_access_key(UserName=username)
        print(f"Access key created for user {username}:")
        print(f"Access Key ID: {create_access_key_response['AccessKey']['AccessKeyId']}")
        print(f"Secret Access Key: {create_access_key_response['AccessKey']['SecretAccessKey']}")

    except Exception as e:
        print(f"Error creating user {username}: {e}")# List of users to create

    return 0

def attach_policy(username):
    # Create the policy
    try:
        print(f"Creating policy: {policy_name}...")
        create_policy_response = iam.create_policy(
            PolicyName=policy_name,
            PolicyDocument=str(policy_document).replace("'", "\"")  # Convert to JSON string
        )
        print(f"Policy created successfully with ARN: {create_policy_response['Policy']['Arn']}")
    except iam.exceptions.EntityAlreadyExistsException:
        print(f"Policy {policy_name} already exists, skipping creation.")
        policy_arn = f"arn:aws:iam::aws:policy/{policy_name}"

    return 0
    
    
if __name__ == '__main__':
    # Loop through the user names and create each user
    for user_name in users:
        try:
            # Create the user
            response = iam.create_user(user_info["username"])
            print(f"User {user_name} created successfully.")
        except Exception as e:
            print(f"Error creating user {user_name}: {e}")

    # Attach the policy to each user
    for user_info in users:
        try:
            print(f"Attaching policy to user: {user_info['username']}...")
            iam.attach_user_policy(
                UserName=user_info['username'],
                PolicyArn=create_policy_response['Policy']['Arn']
            )
            print(f"Policy attached to {user_info['username']} successfully.")
        except Exception as e:
            print(f"Error attaching policy to {user_info['username']}: {e}")
    
    print("Users created and policy attached successfully!")

    
