import boto3
import datetime

# --- Connect to AWS services in your chosen region ---
REGION = 'eu-north-1'  # Replace with your EC2/S3 region
ec2 = boto3.client('ec2', region_name=REGION)
s3 = boto3.client('s3', region_name=REGION)
cloudwatch = boto3.client('cloudwatch', region_name=REGION)


def get_ec2_cpu(instance_id):
    """
    Fetches average CPU utilization for the last hour for a specific EC2 instance.
    Only returns live metrics from CloudWatch. No simulated fallback.
    """
    end_time = datetime.datetime.utcnow()
    start_time = end_time - datetime.timedelta(hours=1)

    try:
        # Request CPU metrics from CloudWatch
        metrics = cloudwatch.get_metric_statistics(
            Namespace='AWS/EC2',
            MetricName='CPUUtilization',
            Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
            StartTime=start_time,
            EndTime=end_time,
            Period=300,  # 5-minute intervals
            Statistics=['Average']
        )

        # Debug: check CloudWatch response
        print(f"CloudWatch metrics for EC2 {instance_id}:", metrics)

        cpu_values = [point['Average'] for point in metrics['Datapoints']]

        if not cpu_values:
            print("Warning: CloudWatch returned no CPU data.")
            return []

        return cpu_values

    except Exception as e:
        print(f"Error fetching EC2 CPU metrics: {e}")
        return []


def get_s3_storage(bucket_name):
    """
    Returns the total storage size (bytes) of an S3 bucket.
    Only uses live data. Returns 0 if bucket is empty or inaccessible.
    """
    try:
        total_size = 0
        response = s3.list_objects_v2(Bucket=bucket_name)

        # Debug: check S3 response
        print(f"S3 response for bucket {bucket_name}:", response)

        if 'Contents' in response:
            for obj in response['Contents']:
                total_size += obj['Size']

        return total_size

    except Exception as e:
        print(f"Error fetching S3 storage: {e}")
        return 0
