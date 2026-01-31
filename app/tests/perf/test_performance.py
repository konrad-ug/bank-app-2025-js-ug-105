import unittest
import requests

# r = requests.get('https://reqbin.com/echo', timeout=5)
# 
# print(f"Status Code: {r.status_code}")
class TestPerfomance():
    imie = "darek"
    nazwisko = "januszewski"
    pesel = "79103075873"
    email = "email@email.pl"
    url = "http://localhost:5001/api/accounts"


    def test_create_and_delete_accounts_performance(self):
        for _ in range(100):
            create_response = requests.post(
                self.url,
                json={"first_name": self.imie, "last_name": self.nazwisko, "pesel": self.pesel, "email": self.email},
                timeout=2
            )

            assert create_response.status_code == 201
            assert create_response.elapsed.total_seconds() < 2

            delete_url = f"{self.url}/{self.pesel}"
            delete_response = requests.delete(delete_url, timeout=2)

            assert delete_response.status_code == 200
            assert delete_response.elapsed.total_seconds() < 2
