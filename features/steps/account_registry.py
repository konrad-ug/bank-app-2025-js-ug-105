from behave import *
import requests

URL = "http://localhost:5000"

@step('I create an account using first_name: "{name}", last_name: "{last_name}", pesel: "{pesel}", email: "{email}"')
def create_account(context, name, last_name, pesel, email):
    json_body = { "first_name": f"{name}",
    "last_name": f"{last_name}",
    "pesel": f"{pesel}",
    "email": f"{email}"
    }
    create_resp = requests.post(f"{URL}/api/accounts", json = json_body)
    assert create_resp.status_code == 201

@step('Account registry is empty')
def clear_account_registry(context):
    response = requests.get(f"{URL}/api/accounts")
    accounts = response.json()

    for account in accounts:
        pesel = account["pesel"]
        requests.delete(f"{URL}/api/accounts/{pesel}")

@step('Number of accounts in registry equals: "{count}"')
def is_account_count_equal_to(context, count):
    response = requests.get(f"{URL}/api/accounts/count")
    number = response.json()
    
    assert number["count"] == int(count)

@step('Account with pesel "{pesel}" exists in registry')
def check_account_with_pesel_exists(context, pesel):
    response = requests.get(f"{URL}/api/accounts/{pesel}")
    assert response.status_code == 200

@step('Account with pesel "{pesel}" does not exist in registry')
def check_account_with_pesel_does_not_exist(context, pesel):
    response = requests.get(f"{URL}/api/accounts/{pesel}")
    assert response.status_code == 404

@when('I delete account with pesel: "{pesel}"')
def delete_account(context, pesel):
    response = requests.delete(f"{URL}/api/accounts/{pesel}")
    assert response.status_code == 200

@when('I update "{field}" of account with pesel: "{pesel}" to "{value}"')
def update_field(context, field, pesel, value):
    if field not in ["first_name", "last_name"]:
        raise ValueError(f"Invalid field: {field}. Must be 'first_name' or 'last_name'.")
    json_body = { f"{field}": f"{value}" }
    response = requests.patch(f"{URL}/api/accounts/{pesel}", json = json_body)
    assert response.status_code == 200

@then('Account with pesel "{pesel}" has "{field}" equal to "{value}"')
def field_equals_to(context, pesel, field, value):
    if field not in ["first_name", "last_name", "pesel", "email"]:
        raise ValueError(f"Invalid field: {field}. Must be 'first_name' or 'last_name', 'pesel' or 'email'.")
    response = requests.get(f"{URL}/api/accounts/{pesel}")
    body = response.json()[0]
    assert body[f"{field}"] == f"{value}"