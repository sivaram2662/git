# import boto3
# available_regions = boto3.Session().get_available_regions('rds')

# for region in available_regions:
#     rds = boto3.client('rds', region_name="us-west-2")
#     paginator = rds.get_paginator('describe_db_instances').paginate()
#     for page in paginator:
#         for dbinstance in page['DBInstances']:
#             print("{DBInstanceClass}".format(**dbinstance))

import boto3
rds = boto3.client('rds')
try:
# get all of the db instances
    dbs = rds.describe_db_instances()
    for db in dbs['DBInstances']:
        print ("%s@%s:%s %s") % (
            db['MasterUsername'],
            db['Endpoint']['Address'],
            db['Endpoint']['Port'],
            db['DBInstanceStatus'])
except Exception as error:
    print (error)