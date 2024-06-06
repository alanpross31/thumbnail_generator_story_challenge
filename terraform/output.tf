output "original_images_bucket_name" {
  description = "The name of the S3 bucket for original images"
  value       = aws_s3_bucket.original_images.bucket
}

output "thumbnails_bucket_name" {
  description = "The name of the S3 bucket for thumbnails"
  value       = aws_s3_bucket.thumbnails.bucket
}

output "lambda_function_name" {
  description = "The name of the Lambda function"
  value       = aws_lambda_function.thumbnail_generator.function_name
}

output "lambda_function_arn" {
  description = "The ARN of the Lambda function"
  value       = aws_lambda_function.thumbnail_generator.arn
}

output "api_gateway_url" {
  description = "The URL of the API Gateway"
  value       = aws_api_gateway_deployment.api.invoke_url
}

output "api_gateway_rest_api_id" {
  description = "The ID of the API Gateway REST API"
  value       = aws_api_gateway_rest_api.api.id
}
