import boto3

# Initialize the IAM client
iam = boto3.client('iam')

# List of users to delete
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

# Function to remove IAM users
def remove_user_and_keys(user_info):
    try:
        # List the user's access keys
        access_keys = iam.list_access_keys(UserName=user_info['username'])['AccessKeyMetadata']
        
        # Delete the user's access keys
        for key in access_keys:
            print(f"Deleting access key for {user_info['username']}...")
            iam.delete_access_key(
                UserName=user_info['username'],
                AccessKeyId=key['AccessKeyId']
            )
            print(f"Access key {key['AccessKeyId']} deleted.")
        
        # Detach the custom policy from the user
        print(f"Detaching policy from {user_info['username']}...")
        iam.detach_user_policy(
            UserName=user_info['username'],
            PolicyArn='arn:aws:iam::aws:policy/S3_EC2_Create_Policy'  # Change if your policy ARN is different
        )
        print(f"Policy detached from {user_info['username']}.")

        # Delete the IAM user
        print(f"Deleting IAM user {user_info['username']}...")
        iam.delete_user(
            UserName=user_info['username']
        )
        print(f"User {user_info['username']} deleted successfully.\n")
    
    except Exception as e:
        print(f"Error removing user {user_info['username']}: {e}")

if __name__ == '__main__':
    # Loop through each user and delete
    for user_info in users:
        remove_user_and_keys(user_info)
    
    print("All specified users and associated resources have been removed.")
