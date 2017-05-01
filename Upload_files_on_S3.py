#/usr/bin/python3.4
import boto3
import time

startTime = time.time()
client = boto3.client('s3')
s3 = boto3.resource('s3')
response = client.list_buckets()
list_of_buckets = ['sample.txt', 'sample2.txt', 'process.py']
#To list the buckets exists in account
#for i in (response['Buckets']):
    #print (i['Name'])
for i in list_of_buckets:
    s3.meta.client.upload_file( i, 'bucket-name', i)
print ('The script took {0} second !'.format(time.time() - startTime))
