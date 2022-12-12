# import boto3
# session = boto3.Session('ec2',AWS_REGION='ap-southeast-1')
# client=session.client('ec2')
# all_regions=client.describe_regions()
# for ec2 in all_regions['regions']:
#     print(ec2['RegionName'])



import boto3
session=boto3.session(profile_name="aws_ec2_iam_user",region_name='us-east-1')
client=session.client(service_name='ec2')
all_regions=client.describe_regions()
for each_reg in all_regions['Regions']:
    print(each_reg['RegionName'])