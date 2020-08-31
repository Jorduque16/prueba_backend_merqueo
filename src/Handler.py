import jmespath

from Controllers.DistributionController import DistributionController
from Exceptions import ExceptionHandler
from Models.ModelFactory import ModelFactory


@ExceptionHandler.handler
def process(event, context):
    model = ModelFactory.get_model('mysql')
    order_id = jmespath.search('pathParameters.id', event)
    distribution_controller = DistributionController(model)
    order_products = model.get_order_products(order_id=order_id)
    provider_list = distribution_controller.get_provider_list()
    distribution = distribution_controller.build_distribution(provider_list, order_products)
    return distribution
