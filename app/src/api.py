from flask import Flask, request, jsonify
import pytest
from src.account_registry import AccountRegistry
from src.personal_account import PersonalAccount
app = Flask(__name__)
registry = AccountRegistry()

@app.route("/api/accounts", methods=['POST'])
def create_account():
    data = request.get_json()
    print(f"Create account request: {data}")
    account = PersonalAccount(data["first_name"], data["last_name"], data["pesel"], data["email"])
    if not registry.add_account(account):
        return jsonify({"message": "Cannot create an account with duplicate pesel"}), 409
    
    return jsonify({"message": "Account created"}), 201
    
@app.route("/api/accounts", methods=['GET'])
def get_all_accounts():
    print("Get all accounts request received")
    accounts = registry.get_accounts()
    accounts_data = [{"first_name": acc.first_name, "last_name": acc.last_name, "pesel":
    acc.pesel, "email": acc.email, "balance": acc.balance} for acc in accounts]
    return jsonify(accounts_data), 200

@app.route("/api/accounts/count", methods=['GET'])
def get_account_count():
    print("Get account count request received")
    count = registry.get_number_of_accounts()
    return jsonify({"count": count}), 200

@app.route("/api/accounts/<pesel>", methods=['GET'])
def get_account_by_pesel(pesel):
    account = registry.find_account_by_pesel(pesel)
    if account is None:
        return jsonify({"message": "Account not found"}), 404
    
    account_data = [{
        "first_name": account.first_name,
        "last_name": account.last_name,
        "pesel": account.pesel,
        "email": account.email, 
        "balance": account.balance
    }]
    return jsonify(account_data), 200

@app.route("/api/accounts/<pesel>", methods=['PATCH'])
def update_account(pesel):
    data = request.get_json()
    updated = False

    for key, value in data.items():
        if registry.update_account_data(pesel, key, value):
            updated = True

    if not updated:
        return jsonify({"message": "Could not update account"}), 404
    
    return jsonify({"message": "Account updated"}), 200

@app.route("/api/accounts/<pesel>", methods=['DELETE'])
def delete_account(pesel):
    if not registry.delete_account(pesel):
        return jsonify({"message": "Account could not be removed"}), 404
    
    return jsonify({"message": "Account deleted"}), 200

@app.route("/api/accounts/<pesel>/transfer", methods=['POST'])
def transfer(pesel):
    data = request.get_json()
    account = registry.find_account_by_pesel(pesel)

    if account is None:
        return jsonify({"message": "Account not found"}), 404
    
    if data["type"] == "incoming":
        if account.incoming_transfer(data["amount"]):
            return jsonify({"message": "Zlecenie przyjęte do realizacji"}), 201
        return jsonify({"message": "Wystąpił błąd realizacji przelewu"}), 404
    elif data["type"] == "outgoing" and account.outgoing_transfer(data["amount"]):
        return jsonify({"message": "Zlecenie przyjęte do realizacji"}), 201
    elif data["type"] == "express" and account.outgoing_transfer(data["amount"], True):
        return jsonify({"message": "Zlecenie przyjęte do realizacji"}), 201
    
    return jsonify({"message": "Wystąpił błąd przy zlecaniu przelewu"}), 422

@app.route("/api/accounts/save", methods=['PATCH'])
def save_to_db():
   registry.save()
   return jsonify({"message": "accounts were saved to db"}), 200

@app.route("/api/accounts/load", methods=['PATCH'])
def load_from_db():
   registry.load()
   return jsonify({"message": "accounts loaded from db"}), 200