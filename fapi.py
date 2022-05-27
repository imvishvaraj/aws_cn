import json
import boto3
from fastapi import FastAPI, Request


# reading config file
cfile = open("/Users/vishvaraj/configs/aws_opcito.json", 'r')
configs = json.loads(cfile.read())


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/ec2/")
async def create_ec2(request: Request):
    req_data = await request.json()
    ec2 = boto3.client(
        "ec2",
        req_data.get("region_name", "us-east-1"),
        aws_access_key_id=configs["ACCESS_KEY_ID"],
        aws_secret_access_key=configs["SECRET_ACCESS_KEY"]
    )
    resp = ec2.run_instances(
        InstanceType=req_data.get("InstanceType", "t2.micro"),
        MaxCount=1,
        MinCount=1,
        ImageId="ami-0022f774911c1d690"
    )
    context = {}
    for row in resp['Instances']:
        context['InstanceId'] = row['InstanceId']
        context['InstanceType'] = row['InstanceType']

    return context


@app.get("/ec2/")
def list_ec(request: Request):
    ec2_r = boto3.resource("ec2", region_name="us-east-1")
    instances = ec2_r.instances.all()

    data = []
    for instance in instances:
        row = {}
        row["instances_id"] = instance.id
        row["Instance Id"] = instance.id
        row['Instance state'] = instance.state["Name"]
        row['Instance AMI'] = instance.image.id
        row['Instance platform'] = instance.platform
        row['Instance type'] = instance.instance_type
        row['Public IPv4 address'] = instance.public_ip_address
        data.append(row)

    return {"AWS EC2 Instances": data}


@app.delete("/ec2/")
async def remove_ec2(request: Request):
    req_data = await request.json()
    instance_ids = req_data.get("instance_ids", None)
    print(instance_ids)
    ec2_r = boto3.resource("ec2", region_name="us-east-1")
    context = {}

    if instance_ids:
        if isinstance(instance_ids, str):
            # instance_ids = [instance_ids]
            inst = ec2_r.Instance(instance_ids)
            inst.terminate()
            context[instance_ids] = "DELETED"

        if isinstance(instance_ids, list):
            for id in instance_ids:
                inst = ec2_r.Instance(id)
                inst.terminate()
                context[id] = "DELETED"

        return context
    else:
        return {"message": "Please provide EC2 Instance ID or list of IDs."}


@app.get("/s3/")
async def list_s3_buckets(request: Request):
    context = {}
    try:
        s3_r = boto3.client(
            "s3",
            region_name="us-east-1"
        )
        response = s3_r.list_buckets()
        context['message'] = "List of s3 buckets in current region."
        context["Buckets List"] = []
        for bucket in response['Buckets']:
            context["Buckets List"].append(bucket['Name'])
        return context
    except Exception as e:
        context['message'] = "Failed to retrieve list of s3 bucket in current region."
        context["error"] = str(e)
        return context


@app.post("/s3/{bucket_name}/")
async def create_s3_bucket(bucket_name):
    context = {}
    try:
        s3_r = boto3.client(
            "s3",
            region_name="us-east-1"
        )
        res = s3_r.create_bucket(Bucket=bucket_name)
        context["message"] = f"Bucket Created as {bucket_name}"
        context["data"] = res
        return context
    except Exception as e:
        context["message"] = "Failed to create bucket."
        context["error"] = str(e)
        return context


@app.delete("/s3/{bucket_name}/")
async def delete_s3_bucket(bucket_name: str):
    context = {}
    try:
        s3_r = boto3.client(
            "s3",
            region_name="us-east-1"
        )
        res = s3_r.delete_bucket(Bucket=bucket_name)
        context["message"] = f"{bucket_name} bucket deleted!"
        context["data"] = res
        return context
    except Exception as e:
        context["message"] = "Failed to delete bucket."
        context["error"] = str(e)
        return context

