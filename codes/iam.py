# import boto3
# import csv
# iam_obj=boto3.resource('iam')
# for iam_user in iam_obj.users.all():
    
#     print(iam_user.name)    
#     header=['user_name']
#     with open ('iam-details.csv', 'w') as file:
#         writer = csv.DictWriter(file, fieldnames=header)
#         writer.writeheader()
#         writer.writerows()   
# import boto3 
# s3 = boto3.client("s3")
# all_objects = s3.list_objects(Bucket = 'manchinti')     
       
    
        
        
import boto3
import csv
iam_obj=boto3.resource('iam')
iam = boto3.resource('iam')
fo=open('iam.userdetails.csv','w',newline='')
data_obj=csv.writer(fo, delimiter=",")
data_obj.writerow([ 'user_name'])
for iam_user in iam_obj.users.all():
  data_obj.writerow([iam_user.name])
fo.close()
 
 
 

     
  