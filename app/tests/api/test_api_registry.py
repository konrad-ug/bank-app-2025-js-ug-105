import pytest
import requests

BASE_URL = "http://localhost:5000"

def clear_registry():
    r = requests.get(f"{BASE_URL}/api/accounts")
    for acc in r.json():
        requests.delete(f"{BASE_URL}/api/accounts/{acc['pesel']}")

def test_save_and_load_accounts():
    clear_registry()

    create_resp = requests.post(
        f"{BASE_URL}/api/accounts",
        json={
            "first_name": "Jan",
            "last_name": "Kowalski",
            "pesel": "12345678901",
            "email": "email@email.pl"
        }
    )
    assert create_resp.status_code == 201

    save_resp = requests.patch(f"{BASE_URL}/api/accounts/save")
    assert save_resp.status_code == 200

    delete_resp = requests.delete(f"{BASE_URL}/api/accounts/12345678901")
    assert delete_resp.status_code == 200

    count_resp = requests.get(f"{BASE_URL}/api/accounts/count")
    assert count_resp.json()["count"] == 0

    load_resp = requests.patch(f"{BASE_URL}/api/accounts/load")
    assert load_resp.status_code == 200

    get_resp = requests.get(f"{BASE_URL}/api/accounts/12345678901")
    assert get_resp.status_code == 200
