import os

from Exceptions.DriverNotConfigured import DriverNotConfigured
from Models.MySQLModel import MySQLModel


class ModelFactory:
    @staticmethod
    def get_model(driver: str):
        available_drivers = {
            "mysql": MySQLModel(host=os.environ['DATABASE_HOST'],
                                database=os.environ['DATABASE_NAME'],
                                user=os.environ['DATABASE_USERNAME'],
                                password=os.environ['DATABASE_PASSWORD'])
        }
        driver_instance = available_drivers.get(driver, None)
        if not driver_instance:
            raise DriverNotConfigured(driver)
        return driver_instance
