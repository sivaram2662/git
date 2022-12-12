import collections
import boto3
import datetime
import pygsheets

REGIONS = ('us-west-2',)
REGIONS_H = ('Oregon',)

currentDT = str(datetime.datetime.now())


def create_spreadsheet(outh_file, spreadsheet_name = "AWS usage"):
    client = pygsheets.authorize(outh_file=outh_file, outh_nonlocal=True)
    client.list_ssheets(parent_id=None)
    spread_sheet = client.create(spreadsheet_name)
    return spread_sheet


def rds_worksheet_creation(spread_sheet):
    for i in range(len(REGIONS)):
        region = REGIONS[i]
        region_h = REGIONS_H[i]
        print()
        print("{} instances in {}".format("RDS", region_h))
        print("------------------------------")

        client = boto3.client('rds', region_name=region)
        db_instances = client.describe_db_instances()
        for i in range(len(db_instances)):
            j = i - 1
            try:
                DBName = db_instances['DBInstances'][j]['DBName']
            except KeyError:
                DBName = "+++ DBName gave KeyError +++"
            MasterUsername = db_instances['DBInstances'][0]['MasterUsername']
            DBInstanceClass = db_instances['DBInstances'][0]['DBInstanceClass']
            DBInstanceIdentifier = db_instances['DBInstances'][0]['DBInstanceIdentifier']
            Endpoint = db_instances['DBInstances'][0]['Endpoint']
            Address = db_instances['DBInstances'][0]['Endpoint']['Address']
            print("{} {} {} {} {}".format(Address, MasterUsername, DBName, DBInstanceClass,
            DBInstanceIdentifier))


if __name__ == "__main__":
    spread_sheet = create_spreadsheet(spreadsheet_name = "AWS usage", outh_file = '../client_secret.json')
    spread_sheet.link(syncToCloud=False)
    rds_worksheet_creation(spread_sheet)