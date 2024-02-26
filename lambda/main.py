import os

def handler(event, context):
    response_body = {
        "message": "Hello World",
        "version": "1.0.0"
    }
    
    # Kirim respons dengan status code 200 dan menggunakan response_body
    return {
        "statusCode": 200,
        "body": response_body
    }
