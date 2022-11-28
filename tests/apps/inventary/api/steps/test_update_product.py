import pytest
from pytest_bdd import scenario

FEAUTRE_NAME = "../features/products/update_product.feature"


@pytest.mark.feature
@scenario(
    feature_name=FEAUTRE_NAME,
    scenario_name="A non-existent product",
)
def test_update_non_existent_product():
    ...


@pytest.mark.feature
@scenario(
    feature_name=FEAUTRE_NAME,
    scenario_name="A existent product",
)
def test_update_existent_product():
    ...
