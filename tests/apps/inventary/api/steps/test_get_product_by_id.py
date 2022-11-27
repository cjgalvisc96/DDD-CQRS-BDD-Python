import pytest
from pytest_bdd import scenario


@pytest.mark.feature
@scenario(
    "../features/products/get_product_by_id.feature",
    "A non-existent product",
)
def test_get_non_existent_product():
    ...


@pytest.mark.feature
@scenario(
    "../features/products/get_product_by_id.feature",
    "A existent product",
)
def test_get_existent_product():
    ...
