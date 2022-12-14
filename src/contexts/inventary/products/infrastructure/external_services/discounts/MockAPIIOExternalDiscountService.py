from random import randint

import httpx

from .ExternalDiscountService import ExternalDiscountService


class MockAPIIOExternalDiscountService(ExternalDiscountService):
    def __init__(self, *, url: str) -> None:
        self.url = url

    async def get_discount_percentage(self, *, product_id: str) -> int:
        async with httpx.AsyncClient() as client:
            try:
                request_discount = await client.get(
                    url=f"{self.url}/{randint(1, 41)}"
                )
            except httpx.HTTPError:
                return 0

        if request_discount.status_code != 200:
            return 0

        return int(request_discount.json().get("discount", 0))
