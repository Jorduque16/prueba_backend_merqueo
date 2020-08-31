class RecordNotFoundException(Exception):
    def __init__(self, causes):
        Exception.__init__(self, causes)
