import requests
from login_data import login

class WorldCupApi:
    def __init__(self, login_data):
        self.base_url="http://api.cup2022.ir/api/v1/"
        self.headers = {'Content-Type': 'application/json'}
        self.login_data = login_data

    def login (self):
        url = self.base_url
        url +="user/login"
        
        response = requests.post(url, headers=self.headers, json=self.login_data)
        print(response)
        r = response.json()
        token = r.get('data').get('token')
        return token

cup = WorldCupApi(login)
t = cup.login()
print(t)