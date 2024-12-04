"""An AWS Python Pulumi program"""
import pulumi
import json
import iam
import pulumi_aws as aws
from ecr import image

lambda_function_name = "lambdaFunction"

# Create the lambda to execute
lambda_function = aws.lambda_.Function(lambda_function_name,
    package_type="Image",
    image_uri=image.image_uri,
    runtime="python3.8",
    timeout=900,
    role=iam.lambda_role.arn)

# Give API Gateway permissions to invoke the Lambda
lambda_permission = aws.lambda_.Permission("lambdaPermission", 
    action="lambda:InvokeFunction",
    principal="apigateway.amazonaws.com",
    function=lambda_function)

# Set up the API Gateway
apigw = aws.apigatewayv2.Api("httpApiGateway", 
    protocol_type="HTTP",
    route_key="POST /",
    target=lambda_function.invoke_arn)

# Export the API endpoint for easy access
pulumi.export("endpoint", apigw.api_endpoint)