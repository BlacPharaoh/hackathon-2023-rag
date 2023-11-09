aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.us-east-1.amazonaws.com
docker tag image_id aws_account_id.dkr.ecr.us-east-1.amazonaws.com/llama2-lambda:v1
docker push aws_account_id.dkr.ecr.us-east-1.amazonaws.com/llama2-lambda:v1