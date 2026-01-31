from flask import Flask, request, jsonify
from src.api import app
from src.account_registry import AccountRegistry
from src.personal_account import PersonalAccount
import pytest

@pytest.fixture()
def sample_account():
    return {
            "first_name": "Flask",
            "last_name": "dark",
            "pesel": "95612345321",
            "email": "email@email.pl",
            "balance": 100,
        }

@pytest.fixture()
def client():
    return app.test_client()

def test_create_account(client, sample_account):
    client.post('/api/accounts', json=sample_account)
    

@pytest.mark.parametrize(
        "description, pesel, body, expected_status",
        [
            [
                "Incoming transfer no account",
                "95612345320",
                { "amount": 500, "type": "incoming" },
                404,
            ],
            [
                "Incoming transfer correct",
                "95612345321",
                { "amount": 500, "type": "incoming" },
                201,
            ],
            [
                "Incoming transfer incorrect amount",
                "95612345321",
                { "amount": 0, "type": "incoming" },
                404,
            ],
            [
                "Outgoing transfer correct amount",
                "95612345321",
                { "amount": 10, "type": "outgoing" },
                201,
            ],
            [
                "Express transfer correct amount",
                "95612345321",
                { "amount": 10, "type": "express" },
                201,
            ],
            [
                "Outgoing transfer incorrect amount",
                "95612345321",
                { "amount": 0, "type": "outgoing" },
                422,
            ],
            [
                "Express transfer incorrect amount",
                "95612345321",
                { "amount": 0, "type": "express" },
                422,
            ],
        ]
)
def test_transfers_parametrized(client, description, pesel, body, expected_status):
    response = client.post(f'/api/accounts/{pesel}/transfer', json=body)
    assert response.status_code == expected_status

