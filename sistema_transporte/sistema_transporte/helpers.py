def HttpResponse(statusCode, data, message):
    return {
        'statusCode': statusCode,
        'data': data,
        'message': message,

    }