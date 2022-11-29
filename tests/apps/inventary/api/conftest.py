import json
from unittest.mock import AsyncMock

import pytest
import pytest_asyncio
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest_bdd import given, parsers, then

from src.apps.inventary.api import InventaryFastAPI
from src.contexts.inventary import inventary_settings
from src.contexts.inventary.products.infrastructure import MemoryCacheService
from src.contexts.shared.domain import DomainConstants
from tests.contexts.shared import LoggingLoggerMock
from tests.shared.utils import clear_mongo_database, mongo_connection


@pytest.fixture
def logging_logger_mock():
    return LoggingLoggerMock(
        filename="logTest/logsTest.txt",
        name="DomainLoggerTest",
        level=DomainConstants["logger_level"],
        format_=DomainConstants["logger_format"],
        date_format=DomainConstants["logger_date_format"],
    )


@pytest.fixture
def memory_cache_service():
    return MemoryCacheService()


@pytest.fixture
def inventary_test_api(logging_logger_mock, memory_cache_service):
    return InventaryFastAPI(
        host=inventary_settings.API_HOST,
        port=inventary_settings.API_PORT,
        logger=logging_logger_mock,
        db=mongo_connection(),
        cache_service=memory_cache_service,
    )


@pytest_asyncio.fixture()
async def app(inventary_test_api) -> FastAPI:
    client_db = inventary_test_api.db
    cache_service = inventary_test_api.cache_service
    # to simulate start() event
    await client_db.init_db()
    await cache_service.init()

    await clear_mongo_database(mongo_db=client_db.db)
    return inventary_test_api.app


@given(
    parsers.parse(
        'I send a POST request to "{endpoint}" with body:\n{body:json}',
        extra_types=dict(json=json.loads),
    ),
    target_fixture="http_request",
)
def send_post_request(app, endpoint, body):
    with TestClient(app) as client:
        http_request = client.post(url=endpoint, json=body)
    return http_request


@given(
    parsers.parse(
        'I send a PUT request to "{endpoint}" with body:\n{body:json}',
        extra_types=dict(json=json.loads),
    ),
    target_fixture="http_request",
)
def send_put_request(app, endpoint, body):
    with TestClient(app) as client:
        http_request = client.put(url=endpoint, json=body)
    return http_request


@given(
    parsers.parse(
        'I send a GET request to "{endpoint}"',
    ),
    target_fixture="http_request",
)
def send_get_request(monkeypatch, app, endpoint):
    with TestClient(app) as client:
        http_request = client.get(url=endpoint)
    return http_request


@then(
    parsers.parse('The response status code should be "{expected_status:d}"')
)
def check_response_status(http_request, expected_status):
    assert http_request.status_code == expected_status


@then(
    parsers.parse(
        "The response body should be:\n{response_body:json}",
        extra_types=dict(json=json.loads),
    )
)
def check_body_response(http_request, response_body: dict):
    assert http_request.json() == response_body


@then(
    parsers.parse(
        "The response body should be empty",
    )
)
def check_empty_response_body(http_request):
    json_response = http_request.json()
    assert not json_response


@then(
    parsers.parse(
        'Logger DEBUG was called "{call_times:d}" time(s)',
    )
)
def check_logger_debug_calls(logging_logger_mock, call_times: int):
    assert logging_logger_mock.debug_mock.call_count == call_times


@then(
    parsers.parse(
        'Logger INFO was called "{call_times:d}" time(s)',
    )
)
def check_logger_info_calls(logging_logger_mock, call_times: int):
    assert logging_logger_mock.info_mock.call_count == call_times


@given(
    parsers.parse(
        'External discount service with response "{discount:d}"',
    )
)
def external_discount_service_mock(monkeypatch, discount: int):
    monkeypatch.setattr(
        (
            f"src.contexts.inventary.products.infrastructure.external_services."
            f"discounts.MockAPIIOExternalDiscountService."
            f"MockAPIIOExternalDiscountService.get_discount_percentage"
        ),
        AsyncMock(return_value=discount),
    )
