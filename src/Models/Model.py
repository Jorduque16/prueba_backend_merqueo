from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def get_order_products(self, order_id: int) -> list:
        """ This method allows get the order products from an order"""

    @abstractmethod
    def get_providers(self) -> list:
        """ This method allows get the provider list"""

    @abstractmethod
    def get_inventory_products(self) -> list:
        """ This method allows get the stored products in inventory"""

    @abstractmethod
    def get_provider_products(self, provider_id: int) -> list:
        """ This method allows get the provider products"""

    @abstractmethod
    def get_orders(self) -> list:
        """ This method allows get the order list""" \
 \
    @abstractmethod
    def get_top_sold_products(self, sort: str) -> list:
        """ This method allows get the top sold products ordered by total"""
