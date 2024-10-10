import json
import time

from icecream import ic
from config import sqs, queue_url

messages = [
    {
        "id": "msg1",
        "messageBody": {
            "name": "Dhaval Chheda 1",
            "age": 35
        }
    }, {
        "id": "msg2",
        "messageBody": {
            "name": "Dhaval Chheda 2",
            "age": 35
        }
    }, {
        "id": "msg3",
        "messageBody": {
            "name": "Dhaval Chheda 3",
            "age": 35
        }
    }, {
        "id": "msg4",
        "messageBody": {
            "name": "Dhaval Chheda 4",
            "age": 35
        }
    }
]

entries = []

for i, msg in enumerate(messages):
    unique_id = round(time.time() * 1000) + i
    entry = {
        'Id': msg['id'],  # A unique identifier for the message
        'MessageBody': json.dumps(msg['messageBody']),  # Message content
        'MessageGroupId': 'group_1',
        'MessageDeduplicationId': str(unique_id),
    }
    entries.append(entry)

# Send message to SQS queue
# response = sqs.send_message(
#     QueueUrl=queue_url,
#     MessageGroupId='group_1',
#     MessageBody=message_string,  # The message content
#     MessageDeduplicationId=str(round(time.time() * 1000)),
#     # Optional: ensure messages with the same content aren't duplicated
# )
#
# # Print out the response
# ic(response['MessageId'])
# ic(response)

# Send batch of messages to SQS queue
response = sqs.send_message_batch(
    QueueUrl=queue_url,
    Entries=entries,
)

# Print out the response
ic(response)
