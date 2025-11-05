import boto3  # lets Python talk to AWS


#Creating AWS clients, connect to EC2 (virtual servers)
ec2 = boto3.client('ec2')

# Creating AWS clients, connect to S3 (cloud storage)
s3 = boto3.client('s3')

# ask AWS for all EC2 instances you own
ec2_data = ec2.describe_instances()

# show the EC2 instance details in the terminal
print("EC2 Instances:", ec2_data['Reservations'])

# ask AWS for all S3 buckets you own
s3_data = s3.list_buckets()

# show the bucket names in the terminal
print("S3 Buckets:", [bucket['Name'] for bucket in s3_data['Buckets']])
