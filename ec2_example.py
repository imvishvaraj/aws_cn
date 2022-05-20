import os
import json
import json_operations
import boto3

cfile = open("/Users/vishvaraj/configs/aws_opcito.json", 'r')
configs = json.loads(cfile.read())

# CONNECT EC2 AWS CLIENT
ec2 = boto3.client(
    "ec2",
    "us-east-1",
    aws_access_key_id=configs["ACCESS_KEY_ID"],
    aws_secret_access_key=configs["SECRET_ACCESS_KEY"]
)

# conn = ec2.run_instances(
#     InstanceType="t2.micro",
#     MaxCount=1,
#     MinCount=1,
#     ImageId="ami-0022f774911c1d690"
# )

# print(conn)

# list all running ec2 instances
ec2_r = boto3.resource("ec2", region_name="us-east-1")
instances = ec2_r.instances.all()
#
instance_id = None
for instance in instances:
    instances_id = instance.id
#     print(f"EC2 Instance Id: {instance.id}")
#     print(f'Instance state: {instance.state["Name"]}')
#     print(f'Instance AMI: {instance.image.id}')
#     print(f'Instance platform: {instance.platform}')
#     print(f'Instance type: "{instance.instance_type}')
#     print(f'Piblic IPv4 address: {instance.public_ip_address}')

# instance_id = instances[0].id
print(type(instances_id))
# terminate instances
ec2_r.instances.filter(InstanceIds=[instance_id]).terminate()


