import sys

import pytest

sys.path.append('src')
from Providers.Inventory import Inventory


@pytest.mark.parametrize("inventory_quantity, requested_quantity, expected, message",
                         [
                             (5, 8, False, 'Upper quantity'),
                             (8, 5, True, 'lower quantity'),
                             (5, 5, True, 'equal quantity')
                         ])
def test_is_valid_product(inventory_quantity, requested_quantity, expected, message):
    provider = Inventory(name='test', products=[])
    inventory_product = {'product_id': '1', 'name': 'Leche', 'quantity': inventory_quantity, 'date': ''}
    requested_product = {'id': 1, 'product_id': '1', 'quantity': requested_quantity}
    result = provider.is_valid_product(inventory_product, requested_product)
    assert result is expected, message


def test_decrease_quantity():
    products = [
        {'product_id': '1', 'name': 'Leche', 'quantity': 5, 'date': ''},
        {'product_id': '2', 'name': 'Pan', 'quantity': 3, 'date': ''},
        {'product_id': '3', 'name': 'Queso', 'quantity': 3, 'date': ''}
    ]
    provider = Inventory(name='test', products=products)
    requested_product = {'id': 1, 'product_id': '1', 'quantity': 2}
    provider.decrease_quantity(requested_product)
    assert len(provider._products) == 3
    assert 'quantity' in provider._products[0]
    assert provider._products[0].get('quantity') is 3
    assert provider._products[0].get('name') == 'Leche'


def test_remove_product():
    products = [
        {'product_id': '1', 'name': 'Leche', 'quantity': 5, 'date': ''},
        {'product_id': '2', 'name': 'Pan', 'quantity': 3, 'date': ''},
        {'product_id': '3', 'name': 'Queso', 'quantity': 3, 'date': ''}
    ]
    provider = Inventory(name='test', products=products)
    requested_product = {'id': 1, 'product_id': '1', 'quantity': 5}
    provider.decrease_quantity(requested_product)
    assert len(provider._products) == 2
    assert 'quantity' in provider._products[0]
    assert provider._products[0].get('quantity') is 3
    assert provider._products[0].get('name') == 'Pan'


def test_handle():
    products = [
        {'product_id': '1', 'name': 'Leche', 'quantity': 5, 'date': ''},
        {'product_id': '2', 'name': 'Pan', 'quantity': 3, 'date': ''},
        {'product_id': '3', 'name': 'Queso', 'quantity': 3, 'date': ''}
    ]
    provider = Inventory(name='test', products=products)
    requested_product = {'id': 1, 'product_id': '1', 'quantity': 2}
    result = provider.handle(requested_product)
    assert len(provider._products) == 3
    assert 'quantity' in provider._products[0]
    assert provider._products[0].get('quantity') is 3
    assert provider._products[0].get('name') == 'Leche'
    assert 'id' in result
    assert 'product_id' in result
    assert 'quantity' in result
    assert 'provider_name' in result
    assert result.get('provider_name') is 'test'
