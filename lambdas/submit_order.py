import json
import boto3
import uuid
import os

sqs = boto3.client('sqs')
queue_url = os.environ['QUEUE_URL']

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        product = body.get('product')
        quantity = int(body.get('quantity'))

        if not product or quantity <= 0:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Invalid input'})
            }

        order = {
            'id': str(uuid.uuid4()),
            'product': product,
            'quantity': quantity
        }

        sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(order)
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Order received', 'order': order})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }