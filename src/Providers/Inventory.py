from Providers.AbstractProvider import AbstractProvider


class Inventory(AbstractProvider):

    def handle(self, product: dict) -> dict:
        self.decrease_quantity(product)
        return {
            **product,
            'provider_name': self._name,
        }

    def decrease_quantity(self, product: dict):
        for position, stored_product in enumerate(self._products):
            if stored_product.get('product_id') == product.get('product_id'):
                stored_product['quantity'] -= product.get('quantity')
                if stored_product['quantity'] == 0:
                    self._products.pop(position)

    def is_valid_product(self, provider_product, product):
        if provider_product.get('product_id') == product.get('product_id') and \
                provider_product.get('quantity') >= product.get('quantity'):
            return True
        else:
            return False
