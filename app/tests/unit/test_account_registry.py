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

    def test_save_clears_and_inserts_accounts(self, mocker):
        registry = AccountRegistry()
        mock_collection = mocker.Mock()
        registry.collection = mock_collection

        acc1 = PersonalAccount("Jan", "Kowalski", "12345678901", "a@a.pl")
        acc1.balance = 100
        acc1.history = [100]

        acc2 = PersonalAccount("Anna", "Nowak", "45678901234", "b@b.pl")
        acc2.balance = 200
        acc2.history = [200]

        registry.accounts = [acc1, acc2]

        registry.save()

        mock_collection.delete_many.assert_called_once_with({})
        assert mock_collection.insert_one.call_count == 2

    def test_load_replaces_accounts_from_db(self, mocker):
        registry = AccountRegistry()

        mock_collection = mocker.Mock()
        registry.collection = mock_collection

        mock_collection.find.return_value = [
            {
                "first_name": "Jan",
                "last_name": "Kowalski",
                "pesel": "12345678901",
                "email": "a@a.pl",
                "saldo": 100,
                "history": [100]
            }
        ]

        registry.accounts = ["OLD_ACCOUNT"]

        registry.load()

        assert len(registry.accounts) == 1
        acc = registry.accounts[0]

        assert acc.first_name == "Jan"
        assert acc.last_name == "Kowalski"
        assert acc.pesel == "12345678901"
        assert acc.balance == 100
        assert acc.history == [100]
        