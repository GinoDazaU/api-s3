import boto3
import base64

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = event['body']['bucket_name']
    directory_name = event['body']['directory_name']
    file_name = event['body']['file_name']
    file_content = base64.b64decode(event['body']['file_content'])
    s3.put_object(Bucket=bucket_name, Key=f'{directory_name}/{file_name}', Body=file_content)
    return {
        'statusCode': 200,
        'body': f'Archivo {file_name} subido a {bucket_name}/{directory_name}'
    }
