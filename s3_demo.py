import boto3

BUCKET_NAME = "demo-bucket-010624"

s3 = boto3.client("s3")

# List all buckets

buckets_resp = s3.list_buckets()

for bucket in buckets_resp["Buckets"]:
    print(bucket)

# List all objects inside a bucket

objects_resp = s3.list_objects_v2(Bucket = BUCKET_NAME)

for obj in objects_resp["Contents"]:
    print(obj)

# Upload files to a bucket

with open("./apple.png","rb") as f:
    s3.upload_fileobj(f, BUCKET_NAME, "apple_new_upload.png")

# Download files from a bucket

s3.download_file(BUCKET_NAME, "Architecture.png", "downloaded_image.png")

# Download file with Binary data

with open("downloaded_image.png","wb") as f:
    s3.download_fileobj(BUCKET_NAME, "Architecture.png", f)

# Presigned URL to give limited access to an unauthorized user

url = s3.generate_presigned_url(
    "get_object", 
    Params={"Bucket":BUCKET_NAME, "Key":"Architecture.png"},
    ExpiresIn = 30
    )

print(url)

# Create bucket

bucket_location=s3.create_bucket(Bucket="new-destination-bucket-010624")

print(bucket_location)

#Copy objects from a bucket to another bucket

s3.copy_object(
    Bucket="new-destination-bucket-010624",
    CopySource=f"/{BUCKET_NAME}/Architecture.png",
    Key="copiedArchitecture.png"
)

# Get object's metadata

response=s3.get_object(Bucket=BUCKET_NAME,Key="Architecture.png")

print(response)
