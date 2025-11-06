# pick a bucket name (must be globally unique)
export AWS_DEFAULT_REGION=us-east-1
export BUCKET=discharge-ingest-nevin-123
aws s3 mb s3://$BUCKET

# upload your PDF (change the local file path)
aws s3 cp ./discharge.pdf s3://$BUCKET/ingest/discharge.pdf
