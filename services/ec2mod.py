import boto3


class EC2MOD:
    def __init__(self, type="resource", region_name="us-east-1"):
        self.service_name = "ec2"
        if type == "client":
            self.ec2 = boto3.client(self.service_name, region_name=region_name)
        else:
            self.ec2 = boto3.resource(self.service_name, region_name=region_name)

    def create(self,
               instance_type="t2.micro",
               maxcount=1,
               mincount=1,
               imageid="ami-0022f774911c1d690"):
        try:
            return self.ec2.run_instance(
                InstanceType=instance_type,
                MaxCount=maxcount,
                MinCount=mincount,
                ImageId=imageid
            )

        except Exception as ee:
            return {"error": str(ee)}

    def list_instances(self):
        try:
            instances = self.ec2.instances.all()
            instances_data = []
            for instance in instances:
                row = {}
                row["instances_id"] = instance.id
                row["Instance Id"] = instance.id
                row['Instance state'] = instance.state["Name"]
                row['Instance AMI'] = instance.image.id
                row['Instance platform'] = instance.platform
                row['Instance type'] = instance.instance_type
                row['Public IPv4 address'] = instance.public_ip_address
                instances_data.append(row)
            return {"AWS EC2 Instances": instances_data}
        except Exception as ee:
            return {"error": str(ee)}

    def remove(self, instance_ids):
        try:
            removed_instance_ids = {}
            if instance_ids:
                if isinstance(instance_ids, str):
                    inst = self.ec2.Instance(instance_ids)
                    inst.terminate()
                    removed_instance_ids[instance_ids] = "DELETED"

                if isinstance(instance_ids, list):
                    for id in instance_ids:
                        inst = self.ec2.Instance(id)
                        inst.terminate()
                        removed_instance_ids[id] = "DELETED"

                return removed_instance_ids
        except Exception as ee:
            return {"error": str(ee)}
