import sys

import pytest

sys.path.append('src')
from Providers.ExternalProvider import ExternalProvider


@pytest.mark.parametrize("inventory_quantity, requested_quantity, expected, message",
                         [
                             (5, 8, True, 'Upper quantity'),
                             (8, 5, True, 'lower quantity'),
                             (5, 5, True, 'equal quantity')
                         ])
def test_is_valid_product(inventory_quantity, requested_quantity, expected, message):
    provider = ExternalProvider(name='test', products=[])
    inventory_product = {'product_id': '1', 'name': 'Leche'}
    requested_product = {'id': 1, 'product_id': '1', 'quantity': 1}
    result = provider.is_valid_product(inventory_product, requested_product)
    assert result is expected, message
