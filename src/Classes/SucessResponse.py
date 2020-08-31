from Classes.HttpResponse import HttpResponse


class SuccessResponse(HttpResponse):
    def __init__(self, body: dict):
        super().__init__(
            status_code=200,
            body=body
        )
