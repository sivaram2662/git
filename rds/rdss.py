# from email.headerregistry import Address
# import boto3
# import csv

# AWS_REGION = "us-east-2"
# RDS_RESOURCE = boto3.resource('RDS', region_name=AWS_REGION)

# instances = RDS_RESOURCE.instances.all()
# print(instances)
# file=open('rds_instance_new.csv','w',newline='')
# data_obj=csv.writer(file)
# data_obj.writerow(['s.no', 'Address', 'MasterUsername', 'DBName', 'DBInstanceClass',
#             'DBInstanceIdentifier'])
# for instance in instances:
#     print('rds instance:', {instance.id})
#     print('DBInstanceClass:',{instances['DBInstances'][0]['DBInstanceClass']})
#     print('DBInstanceIdentifier:', {instance['DBInstances'][0]['DBInstanceIdentifier']})
#     print('endpoint:',{instance['DBInstances'][0]['Endpoint']})
#     print('Address:',{instances['DBInstances'][0]['Endpoint']['Address']})
#     data_obj.writerow(['rds instance.instance.id,instance.dbinstanceclass,instance.endpoint,instance.address'])

# file.close()

import boto3
import csv 
client = boto3.client('rds')
# id =str(input("enter a rds db identifier"))
response = client.describe_db_instances(
    # DBInstanceIdentifier= id,
    # Filters=[
    #     {
    #         'Name': 'DB identifier',
    #         'Values': [
    #             'string',
    #         ]
    #     },
    # ],
    # MaxRecords=123,
    # Marker='string'
)
# print (type(response))
# print (len(response))
print (response)
# for key,value in response.items():
#     print ("*****************************")
#     print (len(response['DBInstances']))
# print (len(response['DBInstances']))
# instance = response['DBInstances']
# # print (instance)
# print (type(instance))
# print ( instance['SubnetIdentifier'])
import boto3
import csv 
client = boto3.client('rds')
response = client.describe_db_instances()
for value in response['DBParameterGroups']:
    print(f' {value["VpcId"]}')
