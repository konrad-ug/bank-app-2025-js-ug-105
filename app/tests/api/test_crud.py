from flask import Flask, request, jsonify
from src.api import app
from src.account_registry import AccountRegistry
import pytest
import json

@pytest.fixture()
def client():
    return app.test_client()

@pytest.fixture()
def runner():
    return app.test_cli_runner()

@pytest.fixture()
def data():
    return {
            "first_name": "Flask",
            "last_name": "dark",
            "pesel": "95612345321",
            "email": "email@email.pl",
        }

@pytest.mark.parametrize(
    "description, method, url, body, expected_status",
    [
        (
            "POST create account",
            "post",
            "/api/accounts",
            {
                "first_name": "Flask",
                "last_name": "Dark",
                "pesel": "12345678901",
                "email": "email@email.pl",
            },
            201,
        ),
        (
            "POST create account with duplicate pesel",
            "post",
            "/api/accounts",
            {
                "first_name": "Flask",
                "last_name": "Dark",
                "pesel": "12345678901",
                "email": "email@email.pl",
            },
            409,
        ),
        (
            "GET all accounts",
            "get",
            "/api/accounts",
            None,
            200,
        ),
        (
            "GET number of accounts",
            "get",
            "/api/accounts/count",
            None,
            200,
        ),
        (
            "GET account by pesel",
            "get",
            "/api/accounts/12345678901",
            None,
            200,
        ),
        (
            "PATCH update account",
            "patch",
            "/api/accounts/12345678901",
            {"last_name": "Light"},
            200,
        ),
        (
            "PATCH update account wrong data",
            "patch",
            "/api/accounts/1234567890",
            {"last_name": "Light"},
            404,
        ),
        (
            "DELETE account",
            "delete",
            "/api/accounts/12345678901",
            None,
            200,
        ),
        (
            "DELETE accountwith wrong data",
            "delete",
            "/api/accounts/12345678901",
            None,
            404,
        ),
        (
            "GET deleted account",
            "get",
            "/api/accounts/12345678901",
            None,
            404,
        ),
    ],
)
def test_crud_parametrized(
    client, description, method, url, body, expected_status
):
    http_method = getattr(client, method)

    response = (
        http_method(url, json=body)
        if body is not None
        else http_method(url)
    )

    assert response.status_code == expected_status