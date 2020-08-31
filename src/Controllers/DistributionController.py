from Models.Model import Model
from Providers.Default import Default
from Providers.Inventory import Inventory
from Providers.Provider import Provider


class DistributionController:

    def __init__(self, model: Model):
        self._model = model

    def get_provider_list(self):
        provider_list = []
        inventory_products = self._model.get_inventory_products()
        provider_list.append(Inventory(name='inventory', products=inventory_products))

        for provider in self._model.get_providers():
            provider_products = self._model.get_provider_products(provider_id=provider.get('id'))
            provider_list.append(Provider(name=provider.get('name'), products=provider_products))

        provider_list.append(Default(name='default', products=[]))
        return provider_list

    def build_distribution(self, provider_list: list, order_products: list) -> dict:
        distribution = {
            'distribution': []
        }
        for requested_product in order_products:
            for provider in provider_list:
                if provider.has_product(requested_product):
                    distribution['distribution'].append(provider.handle(requested_product))
                    break
        return distribution
