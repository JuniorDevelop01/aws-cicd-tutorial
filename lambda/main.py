def handler(event, context):
    # Proses event sesuai kebutuhan Anda
    print(event)
    
    # Kirim respons dengan status code 200 dan pesan "Hello World!"
    return {
        "statusCode": 200,
        "body": "Hello World!"
    }