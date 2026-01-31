from behave import *
from src.personal_account import PersonalAccount

first_name = "Jan"
last_name = "Kowalski"
pesel = "12345678901"
email = "email@email.pl"

@step('A personal account is created with balance {balance}')
def create_personal_account(context, balance):
    context.account = PersonalAccount(first_name, last_name, pesel, email)
    context.account.balance = int(balance)

@step('An incoming transfer of "{transfer_amount}" received')
def incoming_transfer(context, transfer_amount):
    context.account.incoming_transfer(int(transfer_amount))

@step('An outgoing transfer of {transfer_amount} sent')
def outgoing_transfer(context, transfer_amount):
    context.account.outgoing_transfer(int(transfer_amount))

@step('An express outgoing transfer of {transfer_amount} sent')
def express_outgoing_transfer(context, transfer_amount):
    context.account.outgoing_transfer(int(transfer_amount), True)

@step('The balance should be {expected_balance}')
def check_balance(context, expected_balance):
    assert context.account.balance == int(expected_balance)