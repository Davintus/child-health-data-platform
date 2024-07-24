import json  
import pytest  
from app.app import handler  

def test_lambda_handler_success():  
    event = {  
            'body': json.dumps({'id': '123', 'content': 'Healthy Child'})  
	        }  
		    response = handler(event, None)  
		        
			    assert response['statusCode'] == 200  
			        assert json.loads(response['body'])['message'] == 'Data successfully ingested'  

				def test_lambda_handler_invalid_data():  
				    event = {  
				            'body': json.dumps({'id': '123'})  # Missing 'content'  
					        }  
						    response = handler(event, None)  
						        
							    assert response['statusCode'] == 400  
							        assert json.loads(response['body'])['error'] == 'Invalid input data'
