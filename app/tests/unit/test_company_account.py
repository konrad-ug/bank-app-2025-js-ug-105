import unittest
from unittest.mock import patch
from src.company_account import CompanyAccount
import requests

class TestCreateBankAccount(unittest.TestCase):
    company_name = "JOG"
    nip = "8461627563"
    wrong_nip = "7461617563"

    @patch('src.company_account.CompanyAccount.check_NIP_with_API')
    def test_create_account_with_correct_nip(self, mock_is_nip_correct):
        mock_is_nip_correct.return_value = True
        konto = CompanyAccount(self.company_name, self.nip, "email@email.pl",)
        assert konto.company_name ==self.company_name
        assert konto.nip == self.nip
        assert konto.balance == 0


    def test_create_account_with_wrong_length_nip(self):
        konto = CompanyAccount(self.company_name, "123456789", "email@email.pl",)
        assert konto.nip == "Invalid"


    @patch('src.company_account.CompanyAccount.check_NIP_with_API')
    def test_create_account_with_nip_not_in_gov(self, mock_is_nip_correct):
        mock_is_nip_correct.return_value = False
        with self.assertRaises(ValueError) as context:
            CompanyAccount(self.company_name, "7461617563", "email@email.pl",)
        self.assertIn("Company not registered!!", str(context.exception))