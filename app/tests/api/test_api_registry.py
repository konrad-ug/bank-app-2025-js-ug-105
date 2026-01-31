import pytest
import requests

class TestSaveLoad:
    url = "http://localhost:5000/api/accounts"
    data = { "first_name": "Jan", "last_name": "Kowalski", "pesel": "79103075873", "email": "email@email.pl"}

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        # setup
        requests.post(self.url, json=self.data)
        yield
        # teardown
        requests.delete(f"{self.url}/{self.data['pesel']}")

    def test_save_load_account(self):
        response = requests.patch(f"{self.url}/save")
        assert response.status_code == 200
        
        delete_response = requests.delete(f"{self.url}/{self.data['pesel']}")
        assert delete_response.status_code == 200
        assert requests.get(f"{self.url}/count").json()["count"] == 0

        load_response = requests.patch(f"{self.url}/load")
        assert load_response.status_code == 200 

        get_response = requests.get(f"{self.url}/{self.data['pesel']}")
        assert get_response.status_code == 200
        assert get_response.json() == {'first_name': self.data['first_name'], 'last_name': self.data['last_name'], 'pesel': self.data['pesel'], 'email': self.data['email'], 'balance': 0}