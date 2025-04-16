import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

def lambda_handler(event, context):
    for record in event['Records']:
        try:
            order = json.loads(record['body'])
            print(f"Processing order: {order}")

            table.put_item(Item={
                'id': order['id'],
                'product': order['product'],
                'quantity': order['quantity']
            })

        except Exception as e:
            print(f"Error processing record: {str(e)}")
