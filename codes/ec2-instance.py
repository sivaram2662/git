
# import boto3
# AWS_REGION = "us-east-2"
# EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
# INSTANCE_STATE = 'running'

# instances = EC2_RESOURCE.instances.filter(
#     Filters=[
#         {
#             'Name': 'instance-state-name',
#             'Values': [
#                 INSTANCE_STATE
#             ]
#         }
#     ]
# )

# print(f'Instances in state "{INSTANCE_STATE}":')

# for instance in instances:
#     print(f'  - Instance ID: {instance.id}')



# import boto3
# ec2_instance=boto3.resource('ec2')
# INSTANCE_STATE='running'
# instances=ec2_instance.instances.filter(
#     Filters=[
#         {
#             'name':'instance-state'
#         }
#     ]
# )
# print('instances "{INSTANCE_STATE}":')
# for instance in instances:
#     print(f' -instance id: {instance.id}')



# import boto3
