from abc import ABC, abstractmethod


class Provider(ABC):

    @abstractmethod
    def handle(self, product: dict) -> dict:
        pass

    @abstractmethod
    def has_product(self, product: dict):
        pass

    @abstractmethod
    def is_valid_product(self, provider_product, product):
        pass
