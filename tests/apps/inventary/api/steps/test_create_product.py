import pytest
from pytest_bdd import scenario


@pytest.mark.feature
@scenario(
    "../features/products/create_product.feature",
    "A invalid product_id",
)
def test_create_product_with_invalid_id():
    ...


@pytest.mark.feature
@scenario(
    "../features/products/create_product.feature",
    "A invalid status",
)
def test_create_product_with_invalid_status():
    ...


@pytest.mark.feature
@scenario(
    "../features/products/create_product.feature",
    "A valid non-existent product",
)
def test_create_non_existent_product_with_valid_body():
    ...


@pytest.mark.feature
@scenario(
    "../features/products/create_product.feature",
    "A valid existent product",
)
def test_create_existent_product_with_valid_body():
    ...
