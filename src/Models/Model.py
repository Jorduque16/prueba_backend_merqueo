from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def get_order_products(self, order_id: int) -> list:
        """ This method allows get the order information"""

    @abstractmethod
    def get_providers(self) -> list:
        """ This method allows get the order information"""

    @abstractmethod
    def get_inventory_products(self) -> list:
        """ This method allows get the order information"""

    @abstractmethod
    def get_provider_products(self, provider_id: int) -> list:
        """ This method allows get the order information"""
