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
