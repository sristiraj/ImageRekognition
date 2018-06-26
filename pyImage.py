## This is used to read text from image files using AWS rekognition service
## The image has to be uploaded to a bucket in AWS and the necessary permission needs to be set for a user going to use AWS via boto3

import boto3

if __name__ == "__main__":

    bucket = 'bucket'
    photo = 'inputtext.jpg'

    client = boto3.client('rekognition','us-east-1')

    response = client.detect_text(Image={'S3Object': {'Bucket': bucket, 'Name': photo}})

    textDetections = response['TextDetections']

    for text in textDetections:
        print(text['DetectedText'])

