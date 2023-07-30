import json
import boto3

def lambda_handler(event, context):
    # Retrieve the input data from the event
    id = event['id']
    capital = event['capital']
    date = event['date']

    # Create a DynamoDB client
    dynamodb = boto3.client('dynamodb')

    # Define the DynamoDB table name
    table_name = 'capital-tracker'

    # Prepare the item to be added to DynamoDB
    item = {
        'id': {'S': str(id)},
        'capital': {'N': str(capital)},
        'date': {'S': date}
    }

    try:
        # Write the item to DynamoDB
        dynamodb.put_item(TableName=table_name, Item=item)
        
        # Return a success response
        return {
            'statusCode': 200,
            'body': 'Data successfully written to DynamoDB'
        }
    except Exception as e:
        # Return an error response
        return {
            'statusCode': 500,
            'body': str(e)
        }
