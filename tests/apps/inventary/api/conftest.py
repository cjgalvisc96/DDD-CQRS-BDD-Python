import json

import pytest_asyncio
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest_bdd import given, parsers, then

from src.apps.inventary.api import InventaryAPI
from src.contexts.inventary import inventary_settings
from tests.contexts.shared import LoggingLoggerMock
from tests.shared.utils import clear_mongo_database, mongo_connection


@pytest_asyncio.fixture()
async def app() -> FastAPI:
    mooc_app = InventaryAPI(
        port=inventary_settings.API_PORT,
        logger=LoggingLoggerMock(),
        db=mongo_connection(),
    )
    client_db = mooc_app.db
    await client_db.init_db()  # to simulate start() event
    await clear_mongo_database(mongo_db=client_db.db)
    return mooc_app.app


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
    assert json_response["detail"][0]["msg"] == msg
    assert json_response["detail"][0]["type"] == type


@then(
    parsers.parse(
        "The response body should be empty",
    )
)
def check_empty_response_body(http_request):
    json_response = http_request.json()
    assert not json_response
