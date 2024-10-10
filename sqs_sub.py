import time

from icecream import ic

from config import sqs, queue_url


def listen_to_sqs():
    while True:
        try:
            # Receive message from SQS queue with long polling
            response = sqs.receive_message(
                QueueUrl=queue_url,
                MaxNumberOfMessages=1,  # Maximum messages to fetch
                WaitTimeSeconds=2,  # Long polling (wait for a message for up to 20 seconds)
                MessageAttributeNames=['All'],  # Get all message attributes
                VisibilityTimeout=30  # Visibility timeout (how long before the message is visible again)
            )

            # Check if any messages were received
            if 'Messages' in response:
                for message in response['Messages']:
                    # Process the message
                    ic(f"Message received: {message['Body']}")
                    ic(f"Message Attributes: {message.get('MessageAttributes', 'No attributes')}")

                    # After processing, delete the message from the queue
                    receipt_handle = message['ReceiptHandle']
                    sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)
                    ic("Message deleted.")
            else:
                ic("No messages received, waiting...")
        except Exception as e:
            ic(f"Error receiving message: {e}")
        time.sleep(1)  # Optional: Sleep between polls


# Start listening to SQS queue
listen_to_sqs()
