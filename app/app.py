import json  
import boto3  
import os  

# Initialize AWS clients  
dynamodb = boto3.resource('dynamodb')  
s3 = boto3.client('s3')  

# Environment variables  
DYNAMODB_TABLE = os.environ['DYNAMODB_TABLE']  
S3_BUCKET = os.environ['S3_BUCKET']  

def handler(event, context):  
    print(f"Received event: {json.dumps(event)}")  

        try:  
	        data = json.loads(event['body'])  
		        
			        if 'id' not in data or 'content' not in data:  
				            return {  
					                    'statusCode': 400,  
							                    'body': json.dumps({'error': 'Invalid input data'})  
									                }  

											        # Store data in DynamoDB  
												        table = dynamodb.Table(DYNAMODB_TABLE)  
													        table.put_item(Item=data)  
														        
															        # Store data in S3  
																        s3.put_object(Bucket=S3_BUCKET, Key=f"{data['id']}.json", Body=json.dumps(data))  

																	        return {  
																		            'statusCode': 200,  
																			                'body': json.dumps({'message': 'Data successfully ingested'})  
																					        }  

																						    except Exception as e:  
																						            print(f"Error processing the event: {str(e)}")  
																							            return {  
																								                'statusCode': 500,  
																										            'body': json.dumps({'error': 'Could not process the request'})  
																											            }
