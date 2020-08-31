import sys

sys.path.append('src')
from Providers.Default import Default


def test_is_valid_product():
    provider = Default(name='default', products=[])
    inventory_product = {'product_id': '1', 'name': 'Leche', 'quantity': 1, 'date': ''}
    requested_product = {'id': 1, 'product_id': '1', 'quantity': 2}
    result = provider.is_valid_product(inventory_product, requested_product)
    assert result is True
