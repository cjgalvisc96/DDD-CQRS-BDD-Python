import pytest
from pytest_bdd import scenario

FEAUTRE_NAME = "../features/products/get_product_by_id.feature"


@pytest.mark.feature
@scenario(
    feature_name=FEAUTRE_NAME,
    scenario_name="A non-existent product",
)
def test_get_non_existent_product():
    ...


@pytest.mark.feature
@scenario(
    feature_name=FEAUTRE_NAME,
    scenario_name="A existent product",
)
def test_get_existent_product():
    ...
