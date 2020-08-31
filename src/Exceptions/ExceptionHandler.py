import sys

from Classes.ErrorResponse import ErrorResponse
from Classes.SucessResponse import SuccessResponse
from Exceptions.RecordNotFound import RecordNotFoundException


def handler(func):
    def handle(*args):
        try:
            result = func(*args)
            response = SuccessResponse(body=result)
        except RecordNotFoundException as exception:
            response = ErrorResponse(status_code=404,
                                     message="The requested record was not found.",
                                     causes=exception.args)
        except:
            response = ErrorResponse(status_code=500,
                                     message="Ops! Sorry, we are currently experiencing technical problems, please "
                                             "contact us if the error persists.",
                                     causes=str(sys.exc_info()[1]))
        return response.__dict__

    return handle
