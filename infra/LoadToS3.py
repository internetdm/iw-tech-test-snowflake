
from secrets import aws_access_key,aws_secret_key
import os

import boto3

client = boto3.client(
    's3',
    aws_access_key_id = aws_access_key,
    aws_secret_access_key=aws_secret_key
)

directory = r'C:\Users\Barney\test\input_data_generator\input_data\starter\transactions'
copydirectory = r'C:\Users\Barney\test\input_data_generator\input_data\starter\transactions\copy.json'

copy = open(copydirectory, "w")

for subdir, dirs, files in os.walk(directory):
    for filename in files:
        filepath = subdir + os.sep + filename

        if filepath.endswith(".json"):
            #print (filepath)
            f = open(filepath, "r")
            for line in f:
                copy.write(line)
            f.close()
copy.close()

upload_bucket='bsilvetestireland'
upload_file='2021-01-21/transaction/transaction.json'
client.upload_file(copydirectory,upload_bucket,upload_file)

copydirectorycustomer = r'C:\Users\Barney\test\input_data_generator\input_data\starter\customers.csv'
upload_bucket='bsilvetestireland'
upload_file='2021-01-21/customer/customer.csv'
client.upload_file(copydirectorycustomer,upload_bucket,upload_file)


copydirectoryproduct = r'C:\Users\Barney\test\input_data_generator\input_data\starter\products.csv'
upload_bucket='bsilvetestireland'
upload_file='2021-01-21/products/products.csv'
client.upload_file(copydirectoryproduct,upload_bucket,upload_file)
