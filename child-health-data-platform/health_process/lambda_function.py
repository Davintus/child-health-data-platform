import boto3  
import json  
import os  
import csv  

dynamodb = boto3.resource('dynamodb')  
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])  

def lambda_handler(event, context):  
    s3 = boto3.client('s3')  
        
	    for record in event['Records']:  
	            bucket = record['s3']['bucket']['name']  
		            key = record['s3']['object']['key']  
			            
				            # Fetch the object from S3  
					            response = s3.get_object(Bucket=bucket, Key=key)  
						            data = response['Body'].read().decode('utf-8')  
							            
								            # Process the data (assuming it's CSV)  
									            reader = csv.DictReader(data.splitlines())  
										            for row in reader:  
											                # Store processed record into DynamoDB  
													            table.put_item(Item=row)  

														        return {  
															        'statusCode': 200,  
																        'body': json.dumps('Data processed successfully!')  
																	    }
