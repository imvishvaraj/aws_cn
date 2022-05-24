import json
import boto3
from typing import Union
from fastapi import FastAPI, Request
from pydantic import BaseModel


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
        req_data.get("region_name","us-east-1"),
        aws_access_key_id=configs["ACCESS_KEY_ID"],
        aws_secret_access_key=configs["SECRET_ACCESS_KEY"]
    )
    conn = ec2.run_instances(
        InstanceType="t2.micro",
        MaxCount=1,
        MinCount=1,
        ImageId="ami-0022f774911c1d690"
    )

    return {"data": json.dumps(conn)}


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

    return {"list of ec2": data}


@app.delete("/ec2/instance_id")
async def remove_ec2(instance_id, request: Request):
    ec2_r = boto3.resource("ec2", region_name="us-east-1")
    ec2_r.instances.filter(InstanceIds=[instance_id]).terminate()


