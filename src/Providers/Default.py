from Providers.AbstractProvider import AbstractProvider


class Default(AbstractProvider):
    def has_product(self, product: dict):
        return True

    def is_valid_product(self, provider_product, product):
        return True
