import json


class HttpResponse(object):
    def __init__(self, status_code: int, body: dict):
        self.statusCode = status_code
        self.headers = {
            "Access-Control-Allow-Origin": "*"
        }
        self.body = json.dumps(body)
