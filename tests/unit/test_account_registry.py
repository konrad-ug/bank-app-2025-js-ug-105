from src.account_registry import AccountRegistry
from src.personal_account import PersonalAccount
import pytest

class TestAccountRegistry:
    
    @pytest.fixture
    def sample_account(self):
        return PersonalAccount("Jane", "Doe", "12345678901")

    def test_add_account(self, sample_account):
        registry = AccountRegistry()
        registry.add_account(sample_account)
        assert registry.get_number_of_accounts() == 1
        assert registry.get_accounts()[0] == sample_account

    def test_multiple_accounts(self, sample_account):
        registry = AccountRegistry()
        registry.add_account(sample_account)
        registry.add_account(sample_account)
        assert registry.get_number_of_accounts() == 2
        assert registry.get_accounts() == [sample_account, sample_account]

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