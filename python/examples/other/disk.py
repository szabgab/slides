import os
import dotenv
import boto3
import argparse

dotenv.load_dotenv()

linode_obj_config = {
    "aws_access_key_id": os.getenv("AWS_ACCESS_KEY_ID"),
    "aws_secret_access_key": os.getenv("AWS_SECRET_ACCESS_KEY"),
    "endpoint_url": "https://diggers.us-southeast-1.linodeobjects.com",
}

client = boto3.client("s3", **linode_obj_config)

parser = argparse.ArgumentParser()
parser.add_argument('--upload')
parser.add_argument('--download')
parser.add_argument('--to')
parser.add_argument('--list', action='store_true')
args = parser.parse_args()

if args.list:
    #s3 = boto3.resource('s3')
    #for bucket in s3.buckets.all():
    #    print(bucket.name)

    #response = client.list_buckets()
    #print(response)
    #print(dir(client))
    #exit()
    response = client.list_objects_v2(
        Bucket='cpan-digger',
        #Delimiter='string',
        #EncodingType='url',
        #Marker='string',
        #MaxKeys=123,
        #Prefix='string',
        #RequestPayer='requester',
        #ExpectedBucketOwner='string'
    )
    #print(response)

    exit()

if args.upload:
    if not args.to:
        exit("Usage: --upload also requires the --to flag")
    client.upload_file(
        Filename=args.upload,
        Bucket='cpan-digger',
        Key=args.to)
    exit()

if args.download:
    if not args.to:
        exit("Usage: --download also requires the --to flag")
    try:
        client.download_file(
            Bucket='cpan-digger',
            Key=args.download,
            Filename=args.to)
    except Exception as err:
        # botocore.exceptions.ClientError: An error occurred (404) when calling the HeadObject operation: Not Found
        print(err)
    exit()

parser.print_help()




#res = client.create_bucket(Bucket='temp')
#print(res)

#print(dir(response))
#print(response.keys())  # ResponseMetadata
#for bucket in response['Buckets']:
#    print(bucket['Name'])



