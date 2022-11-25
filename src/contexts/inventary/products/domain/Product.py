from src.contexts.inventary.products.domain import (
    ProductDescription,
    ProductDiscount,
    ProductFinalPrice,
    ProductName,
    ProductPrice,
    ProductStatus,
    ProductStock,
)
from src.contexts.inventary.shared.domain import ProductId


class Product:
    def __init__(
        self,
        product_id: ProductId,
        name: ProductName,
        status: ProductStatus,
        stock: ProductStock,
        description: ProductDescription,
        price: ProductPrice,
        discount: ProductDiscount = 0.0,
        final_price: ProductFinalPrice = 0.0,
    ) -> None:
        self.product_id = product_id
        self.name = name
        self.status = status
        self.stock = stock
        self.description = description
        self.price = price
        self.discount = discount
        self.final_price = final_price

    @staticmethod
    def create(
        *,
        product_id: str,
        name: str,
        status: int,
        stock: int,
        description: str,
        price: float,
        discount: float = 0.0,
        final_price: float = 0.0,
    ):
        product = Product(
            product_id=ProductId(product_id),
            name=ProductName(name),
            status=ProductStatus(status),
            stock=ProductStock(stock),
            description=ProductDescription(description),
            price=ProductPrice(price),
            discount=ProductDiscount(discount),
            final_price=ProductFinalPrice(final_price),
        )
        return product

    def to_primitives(self):
        return {
            "product_id": self.product_id.value,
            "name": self.name.value,
            "status": self.status.value,
            "stock": self.stock.value,
            "description": self.description.value,
            "price": self.price.value,
            "discount": self.discount.value,
            "final_price": self.final_price.value,
        }
