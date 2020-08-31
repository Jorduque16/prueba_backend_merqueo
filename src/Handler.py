import jmespath

from Controllers.DistributionController import DistributionController
from Exceptions import ExceptionHandler
from Models.ModelFactory import ModelFactory
from Providers.Default import Default
from Providers.ExternalProvider import ExternalProvider
from Providers.Inventory import Inventory


@ExceptionHandler.handler
def process(event, context):
    model = ModelFactory.get_model('mysql')
    distribution_controller = DistributionController()

    order_id = jmespath.search('pathParameters.id', event)

    order_products = model.get_order_products(order_id=order_id)
    distribution_controller.set_order_products(order_products)

    inventory_products = model.get_inventory_products()
    inventory = Inventory(name='inventory', products=inventory_products)
    distribution_controller.set_provider(inventory)

    for provider in model.get_providers():
        provider_products = model.get_provider_products(provider_id=provider.get('id'))
        distribution_controller.set_provider(ExternalProvider(name=provider.get('name'), products=provider_products))

    distribution_controller.set_provider(Default(name='default', products=[]))

    distribution = distribution_controller.build_distribution()
    return {
        'distribution': distribution
    }


@ExceptionHandler.handler
def get_inventory_distribution(event, context):
    model = ModelFactory.get_model('mysql')
    distribution_controller = DistributionController()

    inventory_products = model.get_inventory_products()
    inventory = Inventory(name='inventory', products=inventory_products)
    distribution_controller.set_provider(inventory)

    inventory_distribution = {
        'orders': []
    }

    for order in model.get_orders():
        order_products = model.get_order_products(order_id=order.get('id'))
        distribution_controller.set_order_products(order_products)
        inventory_distribution['orders'].append({
            **order,
            'products': distribution_controller.build_distribution()
        })

    return inventory_distribution
