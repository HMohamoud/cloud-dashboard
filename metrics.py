import boto3
import datetime

# connect to EC2 (virtual servers)
ec2 = boto3.client('ec2')

# connect to S3 (cloud storage)
s3 = boto3.client('s3')

#connects to AWS monitoring service (like CPU usage for EC2 or storage)
cloudwatch = boto3.client('cloudwatch')

#Goal is to get CPU usage for an EC2 instance (or simulate it if i dont have an instance).
def get_ec2_cpu(instance_id):
    #Step 1: Define the time range
    end_time = datetime.datetime.utcnow() # Current time (UTC)
    start_time = end_time - datetime.timedelta(hours=1) #1 hour ago

    try:
        # Step 2: Call CloudWatch API to get CPU metrics for an instance
        metrics = cloudwatch.get_metric_statistics(
            Namespace='AWS/EC2', #The service we are monitoring
            MetricName='CPUUtilization',  # The metric we want 
            Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],  # Which EC2
            StartTime=start_time,
            EndTime=end_time,
            Period=300,  # How often to sample (in seconds) → 5 min
            Statistics=['Average']  # Get the average CPU for each interval

        )
        # Step 3: Get the average CPU values from the returned data
        cpu_values = [point['Average'] for point in metrics['Datapoints']]
    
    except Exception:
        # Step 4: If no instance exists or an error happens, simulate CPU values
        cpu_values = [10.5, 20.2, 15.0, 30.1]

    #step 5: Return the list of CPU values
    return cpu_values

