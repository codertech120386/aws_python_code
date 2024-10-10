import os
import time

import boto3
from dotenv import load_dotenv

load_dotenv()

aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
sqs = boto3.client('sqs', region_name='us-east-1',
                   aws_access_key_id=aws_access_key_id,
                   aws_secret_access_key=aws_secret_access_key)

queue_url = "https://sqs.us-east-1.amazonaws.com/163163300224/MyFirstQueue.fifo"
