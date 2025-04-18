import json
import boto3
import uuid
import os

sqs = boto3.client('sqs')
queue_url = os.environ.get('QUEUE_URL', 'MISSING_QUEUE_URL')

def lambda_handler(event, context):
    try:
        print("Event received:", event)

        # Acepta eventos con o sin 'body' key
        if 'body' in event:
            body = json.loads(event['body']) if isinstance(event['body'], str) else event['body']
        else:
            body = event  # viene directamente del navegador con JSON plano

        print("Parsed body:", body)
        
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

        print("Sending to SQS:", order)

        sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(order)
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Order received', 'order': order})
        }

    except Exception as e:
        print("Error in submit_order:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Internal server error', 'error': str(e)})
        }