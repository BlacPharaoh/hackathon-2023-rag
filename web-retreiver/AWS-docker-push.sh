aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 186900524924.dkr.ecr.us-east-1.amazonaws.com
docker tag f7200391d23a 186900524924.dkr.ecr.us-east-.amazonaws.com/llama2-lambda:v1
docker push 186900524924.dkr.ecr.us-east-1.amazonaws.com/llama2-lambda:v1