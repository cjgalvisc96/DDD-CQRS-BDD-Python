import json

import pytest
import pytest_asyncio
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest_bdd import given, parsers, then

from src.apps.inventary.api.InventaryAPI import InventaryAPI
from src.contexts.inventary import inventary_settings
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
def inventary_test_api(logging_logger_mock):
    return InventaryAPI(
        port=inventary_settings.API_PORT,
        logger=logging_logger_mock,
        db=mongo_connection(),
    )


@pytest_asyncio.fixture()
async def app(inventary_test_api) -> FastAPI:
    client_db = inventary_test_api.db
    await client_db.init_db()  # to simulate start() event
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


@then(
    parsers.parse('The response status code should be "{expected_status:d}"')
)
def check_response_status(http_request, expected_status):
    assert http_request.status_code == expected_status


@then(
    parsers.parse(
        'The response body should have msg="{msg}" and type="{type}"',
    )
)
def check_invalid_response_validations_body(http_request, msg: str, type: str):
    json_response = http_request.json()
    if type == "value_error":
        assert json_response["detail"][0]["msg"] == msg
        assert json_response["detail"][0]["type"] == type
    elif type == "domain_error":
        assert json_response["error"] == msg
        assert json_response["type"] == type


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
