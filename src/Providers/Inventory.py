from Providers.AbstractProvider import AbstractProvider


class Inventory(AbstractProvider):

    def is_valid_product(self, provider_product, product):
        if provider_product.get('product_id') == product.get('product_id') and \
                provider_product.get('quantity') >= product.get('quantity'):
            return True
        else:
            return False
