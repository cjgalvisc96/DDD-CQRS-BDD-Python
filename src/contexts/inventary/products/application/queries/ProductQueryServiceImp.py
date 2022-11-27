from src.contexts.inventary.products.domain import ProductReadRepository
from src.contexts.inventary.products.infrastructure.external_services import (
    ExternalDiscountService,
)

from .ProductQueryIdDTO import ProductQueryIdDTO
from .ProductQueryService import ProductQueryService


class ProductQueryServiceImp(ProductQueryService):
    def __init__(
        self,
        repository: ProductReadRepository,
        external_discount_service: ExternalDiscountService,
    ):
        self._repository = repository
        self._external_discount_service = external_discount_service

    @staticmethod
    def _get_final_price(*, price: float, discount: int) -> float:
        if not discount:
            return price

        return price * (100 - discount) / 100

    async def find_product_by_id(
        self, *, product_id: str
    ) -> ProductQueryIdDTO | bool:
        product = await self._repository.find_product_by_id(
            product_id=product_id
        )
        if not product:
            return False

        discount = (
            await self._external_discount_service.get_discount_percentage(
                product_id=product.product_id.value
            )
        )
        return ProductQueryIdDTO(
            product_id=product.product_id.value,
            name=product.name.value,
            status=product.status.value,
            stock=product.stock.value,
            description=product.description.value,
            price=product.price.value,
            discount=discount,
            final_price=self._get_final_price(
                price=product.price.value, discount=discount
            ),
        )
