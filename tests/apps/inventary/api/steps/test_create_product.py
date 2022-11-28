import pytest
from pytest_bdd import scenario

FEAUTRE_NAME = "../features/products/create_product.feature"


@pytest.mark.feature
@scenario(
    feature_name=FEAUTRE_NAME,
    scenario_name="A invalid product_id",
)
def test_create_product_with_invalid_id():
    ...


@pytest.mark.feature
@scenario(
    feature_name=FEAUTRE_NAME,
    scenario_name="A invalid status",
)
def test_create_product_with_invalid_status():
    ...


@pytest.mark.feature
@scenario(
    feature_name=FEAUTRE_NAME,
    scenario_name="A valid non-existent product",
)
def test_create_non_existent_product_with_valid_body():
    ...


@pytest.mark.feature
@scenario(
    feature_name=FEAUTRE_NAME,
    scenario_name="A valid existent product",
)
def test_create_existent_product_with_valid_body():
    ...
