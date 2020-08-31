from Providers.Provider import Provider


class DistributionController:
    _provider_list: list = []
    _order_products: list = []

    def __init__(self):
        self._provider_list = []
        self._order_products = []

    def set_provider(self, provider: Provider):
        self._provider_list.append(provider)

    def set_order_products(self, order_products: list):
        self._order_products = order_products

    def build_distribution(self) -> list:
        distribution = []
        for requested_product in self._order_products:
            for provider in self._provider_list:
                if provider.has_product(requested_product):
                    distribution.append(provider.handle(requested_product))
                    break
        return distribution
