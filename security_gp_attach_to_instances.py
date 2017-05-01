__author__ = 'vijay'

import boto3


client = boto3.client('ec2')
ec2 = boto3.resource('ec2')

list_sg = []
list_ec2 = []

response1 = client.describe_instances()
for reservation in response1["Reservations"]:
    for instance in reservation["Instances"]:
        count = 0
        # This sample print will output entire Dictionary object
        print (instance)
        # This will print will output the value of the Dictionary key 'InstanceId'
        ec = instance["InstanceId"]

        list_ec2.insert(count,ec)

response = client.describe_security_groups()
for i in response['SecurityGroups']:
    count = 0
    sg = i['GroupId']
    list_sg.insert(count,sg)
print (list_sg)
print(list_ec2)
dict_sg={}
for i in list_sg:
    dict_sg[i]=[]
print (dict_sg)
p=list_ec2[0];
instance = ec2.Instance(p)
for i in list_ec2:
    instance = ec2.Instance(i)
    ec2_tags=instance.tags
    for k in ec2_tags:
        if k['Key']=='Name':
            tags=k['Value']
        if len(tags)!=0:
            list_temp_sg=instance.security_groups
            for j in list_temp_sg:
                dict_sg[j['GroupId']].append(tags)
print(dict_sg)
