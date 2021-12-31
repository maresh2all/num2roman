# Convert decimal number to roman numerals
### Task
Create a simple serverless REST API that given a decimal number returns the roman number.
Try out using small client in api_client.py
Please contact me to get the API_KEY if you want to access the online aws lambda
https://75azg34o8g.execute-api.eu-west-1.amazonaws.com/dev


### Goals
- Deploy as AWS Lambda function
- Use unit tests

## REST API
Using FastAPI
Automated docs at http://localhost:8000/docs

API authentication using api_key in header
API_KEY and SECRET are configure in .env file

uvicorn app_api:app --reload
Try out using small client in api_client.py

## venv

python -m venv env
pip install -r requirements.txt

## Create AWS resources
Create resources using AWS CLI
create_aws_lambda_resources.ps

## Run unit tests
Unit tests for the conversion package
python -m unittest discover -v