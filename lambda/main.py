def handler(event, context):
    print(event)
    return {
        "StatusCode": 200,
        "body": "Hello World!"
    }