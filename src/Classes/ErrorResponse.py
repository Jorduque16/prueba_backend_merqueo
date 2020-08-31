from Classes.HttpResponse import HttpResponse


class ErrorResponse(HttpResponse):
    def __init__(self, status_code: int, message: str, causes):
        super().__init__(
            status_code=status_code,
            body={
                "message": message,
                "causes": causes
            }
        )
