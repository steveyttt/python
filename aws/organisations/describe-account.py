import boto3
# import csv

orgClient = boto3.client('organizations')

out_file = open("enriched.csv", mode='w')
my_file = open("basic.txt")

for line in my_file:
    
    if len(line) < 12:
        print("not enough digits")
        continue

    stripped = line.strip()

    response = orgClient.describe_account(AccountId=stripped)

    tuple_response = response["Account"]["Email"], response["Account"]["Id"], response["Account"]["Name"], "\n"
    enriched_response = ', '.join(tuple_response)
    out_file.write(enriched_response)
