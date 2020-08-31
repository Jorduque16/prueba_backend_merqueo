from abc import ABC, abstractmethod


class Model(ABC):

    @abstractmethod
    def get_order_by_id(self, order_id: int):
        """ This method allows get the order information"""

    @abstractmethod
    def get_order_products(self, order_id: int):
        """ This method allows get the order information"""
