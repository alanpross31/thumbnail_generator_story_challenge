# thumbnail_generator_story_challenge
This is a repository with the solution of the Stori Challenge

For this solution I decide to make the deployment with AWS and make the thumbnail generator in python. Unfournatly I couldn't create some features with the thumbnail like a fronted to talk withe the arquitecture, but I think is a good solution to deploy te infraestructure.

The Architecture has this servcies and tool:
1. **S3 Bucket:** Stores the original images.
2. **Lambda Function:** Generates thumbnails from the original images.
3. **S3 Bucket:** Stores the generated thumbnails.
4. **API Gateway:** Triggers the Lambda function.
5. **CloudWatch:** Monitors the Lambda function.
6. **Terraform:** Deploys the infrastructure.

## Setup

### Pre-requisites

- AWS CLI configured
- Terraform installed
- Python 3.8

## Principal features

### Amazon S3 (Simple Storage Service):

Purpose: Stores the images.
Usage: There are two S3 buckets:
Original Images Bucket: Stores the original images uploaded by users.
Thumbnails Bucket: Stores the generated thumbnail images.

### AWS Lambda:

Objective: Runs the code to generate thumbnails.
Usage: When an image is uploaded to the Original Images Bucket, the Lambda function is triggered to create a thumbnail.

### Amazon API Gateway:

Objective: Provides a way to trigger the Lambda function via an HTTP request.
Usage: The frontend (a web page where users upload images) sends a request to the API Gateway, which then triggers the Lambda function.

### Amazon CloudWatch:

Objective: Monitors and logs the Lambda function’s activity.
Usage: Keeps track of the Lambda function's performance and any errors that occur, making it easier to debug issues.


## How It Works Together

User Uploads an Image:
The user uploads an image through the frontend interface.
The image is sent to the API Gateway as an HTTP request.
API Gateway Triggers Lambda:

The API Gateway receives the request and triggers the Lambda function.
This connection allows the web interface to communicate securely with the backend processing.
Lambda Processes the Image:

The Lambda function receives the image.
It downloads the image from the Original Images Bucket in S3.
The function processes the image to create a thumbnail.
Thumbnail is Saved:

The Lambda function uploads the generated thumbnail to the Thumbnails Bucket in S3.
The user can then access the thumbnail from this bucket.

Monitoring and Logging:

CloudWatch logs the activities of the Lambda function. This includes recording when the function is triggered, how long it takes to run, and any errors that occur.
Running the Setup
To run this setup:

### Deploy the Infrastructure with Terraform:

- Terraform script creates and configures all the AWS resources (S3 buckets, Lambda function, API Gateway, etc.).

#### Install Lambda Dependencies:

- Install necessary Python libraries (like boto3 and Pillow) and package them with the Lambda function code.
  
#### Upload Code and Configuration:

- Deploy the packaged Lambda function code to AWS.
- Terraform handles the linking of API Gateway and Lambda, setting up triggers, and configuring permissions.

![arquitecture_stori](https://github.com/alanpross31/thumbnail_generator_story_challenge/assets/70664639/70fe8170-8ab2-493c-9708-deaa7b34f9cf)

## Strengths 
Scalability
-  The system can handle a large number of users at the same time without any issues.
-  Whether there are 10 users or 10,000 users uploading images, the service will work smoothly without slowing down.

Cost Efficiency
-  The system only costs money when it's being used, rather than charging a flat rate regardless of usage.
- This is a cost-effective solution, especially for small businesses or projects with varying amounts of traffic. You save money because you only pay for what you use.

Simplicity
- The system uses services that are managed by AWS, so we don't have to worry about the technical details of maintaining them.
- This makes the system easier to set up and manage, allowing us to focus on building the core functionality rather than worrying about server maintenance.


