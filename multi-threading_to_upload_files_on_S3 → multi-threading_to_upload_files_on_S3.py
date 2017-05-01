#/usr/bin/python3.4
import boto3
import time
import _thread

startTime = time.time()

def upload():
    client = boto3.client('s3')
    s3 = boto3.resource('s3')
    response = client.list_buckets()
    #List of files need to upload on S3
    list_of_buckets = ['sample.txt', 'sample2.txt', 'process.py']
    for i in list_of_buckets:
        s3.meta.client.upload_file( i, 'Your-bucket-name', i)

_thread.start_new_thread( upload, () )

print ('The script took {0} second !'.format(time.time() - startTime))
