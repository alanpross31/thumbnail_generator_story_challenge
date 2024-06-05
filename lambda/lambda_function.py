import boto3
from PIL import Image
import io

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Get the original image
    response = s3.get_object(Bucket=bucket_name, Key=key)
    image_content = response['Body'].read()

    # Create a thumbnail
    image = Image.open(io.BytesIO(image_content))
    image.thumbnail((128, 128))

    # Save the thumbnail
    buffer = io.BytesIO()
    image.save(buffer, 'JPEG')
    buffer.seek(0)

    # Upload the thumbnail to another S3 bucket
    s3.put_object(
        Bucket='thumbnails-bucket',
        Key=f'thumbnail-{key}',
        Body=buffer,
        ContentType='image/jpeg'
    )
    
    return {
        'statusCode': 200,
        'body': 'Thumbnail generated'
    }
