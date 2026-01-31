from src.account_registry import AccountRegistry
from src.personal_account import PersonalAccount
import pytest

class TestAccountRegistry:
    
    @pytest.fixture
    def sample_account(self):
        return PersonalAccount("Jane", "Doe", "12345678901", "email@email.pl",)

    def test_add_account(self, sample_account):
        registry = AccountRegistry()
        registry.add_account(sample_account)
        assert registry.get_number_of_accounts() == 1
        assert registry.get_accounts()[0] == sample_account

    def test_add_account_with_duplicate_pesel(self, sample_account):
        registry = AccountRegistry()
        registry.add_account(sample_account)
        registry.add_account(sample_account)
        assert registry.get_number_of_accounts() == 1
        assert registry.get_accounts() == [sample_account]

    def test_find_account_by_pesel(self, sample_account):
        registry = AccountRegistry()
        registry.add_account(sample_account)
        found_account = registry.find_account_by_pesel("12345678901")
        assert found_account == sample_account

    def test_find_account_by_invalid_pesel(self, sample_account):
        registry = AccountRegistry()
        registry.add_account(sample_account)
        found_account = registry.find_account_by_pesel("00000000000")
        assert found_account is None

    def test_update_account(self, sample_account):
        registry = AccountRegistry()
        registry.add_account(sample_account)
        registry.update_account_data("12345678901", "first_name", "John")
        assert registry.find_account_by_pesel("12345678901").first_name == "John"

    def test_update_account_wrong_data(self, sample_account):
        registry = AccountRegistry()
        registry.add_account(sample_account)
        registry.update_account_data("1234567890", "pesel", "1234")
        assert registry.find_account_by_pesel("12345678901").first_name == "Jane"

    def test_remove_account(self, sample_account):
        registry = AccountRegistry()
        registry.add_account(sample_account)
        registry.delete_account("12345678901")
        assert registry.find_account_by_pesel("12345678901") == None

    def test_remove_account_wrong_data(self, sample_account):
        registry = AccountRegistry()
        registry.add_account(sample_account)
        registry.delete_account("1234567890")
        assert registry.find_account_by_pesel("12345678901") == sample_account
        