from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount
from src.smtp.smtp import SMTPClient
from datetime import datetime
import pytest

@pytest.fixture
def personal_account():
    return PersonalAccount("Jane", "Doe", "12345678901", "email@email.pl")

@pytest.fixture
def company_account():
    return 

class TestSMTP():

    date = datetime.now().date()
    
    @pytest.mark.parametrize(
            "account, expected_subject, expected_text, passed",
            [
                [
                    PersonalAccount("Jane", "Doe", "12345678901", "email@email.pl"),
                    f'Account Transfer History {date}',
                    f'Personal account history: [-10]',
                    True,
                ],
                [
                    PersonalAccount("Jane", "Doe", "12345678901", "email@email.pl"),
                    f'Account Transfer History {date}',
                    f'Personal account history: [-10]',
                    False,
                ],
                [
                    CompanyAccount("Company Name", "1234567890", "email@email.pl"),
                    f'Account Transfer History {date}',
                    f'Company account history: [-10]',
                    True,
                ],
                [
                    CompanyAccount("Company Name", "1234567890", "email@email.pl"),
                    f'Account Transfer History {date}',
                    f'Company account history: [-10]',
                    False,
                ],
            ]
    )
    def test_send_mail(self, account, expected_subject, expected_text, passed, mocker):
        account.balance = 100
        account.outgoing_transfer(10)

        mock_send = mocker.patch("src.smtp.smtp.SMTPClient.send", return_value=passed)
        result = account.send_history_via_email(account.email)
        assert result is passed
        mock_send.assert_called_once()
        subject = mock_send.call_args[0][0]
        text = mock_send.call_args[0][1]

        assert subject == expected_subject
        assert text ==  expected_text

    def test_smtp(self):
        assert SMTPClient.send("subject", "text", "email") == False