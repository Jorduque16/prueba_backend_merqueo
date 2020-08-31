from Providers.Provider import Provider


class AbstractProvider(Provider):
    _products: list = []
    _name: str = ""

    def __init__(self, name: str, products: list):
        self._name = name
        self._products = products

    def handle(self, product: dict) -> dict:
        return {
            **product,
            'provider_name': self._name,
        }

    def has_product(self, product: dict):
        for provider_product in self._products:
            if self.is_valid_product(provider_product, product):
                return True
        return False

    def is_valid_product(self, provider_product, product):
        pass
