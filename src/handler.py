import json


def process(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "status": "success"
        })
    }
