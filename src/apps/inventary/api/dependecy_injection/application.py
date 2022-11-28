from dependency_injector import containers, providers

from src.apps.inventary.api.dependecy_injection import ProductsContainer


class InventaryContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.apps.inventary.api.controllers.ProductCommandController",
            "src.apps.inventary.api.controllers.ProductQueryController",
        ]
    )
    products_package = providers.Container(ProductsContainer)
