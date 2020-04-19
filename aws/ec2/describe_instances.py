import boto3

## https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instances
def listec2instances():

    client = boto3.client('ec2')

    response = client.describe_instances()

    for i in response["Reservations"]:
        print([i][0]["Instances"][0]["InstanceId"])

        for tag in [i][0]["Instances"][0]["Tags"]:
            if tag['Key'] == 'EnterpriseAppID':
                print("Enterprise AppID = ", tag['Value'])

listec2instances()