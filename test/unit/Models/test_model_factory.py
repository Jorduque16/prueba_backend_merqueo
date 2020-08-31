import sys

import pytest

sys.path.append('src')
from Models.ModelFactory import ModelFactory
from Models.MySQLModel import MySQLModel
from Exceptions.DriverNotConfigured import DriverNotConfigured


def test_get_mysql_model():
    driver_instance = ModelFactory.get_model('mysql')
    assert isinstance(driver_instance, MySQLModel)


def test_driver_nor_configured_exception():
    with pytest.raises(DriverNotConfigured):
        ModelFactory.get_model('unknown')
