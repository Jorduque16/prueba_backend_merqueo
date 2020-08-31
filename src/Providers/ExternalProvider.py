from Providers.AbstractProvider import AbstractProvider


class ExternalProvider(AbstractProvider):

    def is_valid_product(self, provider_product, product):
        return provider_product.get('product_id') == product.get('product_id')
