import boto3

orgClient = boto3.client('organizations')

paginator = orgClient.get_paginator('list_accounts')
page_iterator = paginator.paginate()

for page in page_iterator:
    for account in page["Accounts"]:
        print(account['Id'], ',', account["Name"], ',', account["Email"])