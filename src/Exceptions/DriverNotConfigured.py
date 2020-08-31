class DriverNotConfigured(Exception):
    def __init__(self, driver: str):
        Exception.__init__(self, f'The requested driver ({driver}) are not configured.')
