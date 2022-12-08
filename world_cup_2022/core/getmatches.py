import requests
from pprint import pprint

class WorldCupApi:
    def __init__(self):
        self.base_url="https://api.football-data.org/v4/"
        

    def get_matches (self, token):
        
        url = self.base_url
        url += "competitions/2000/matches"
        headers = { 'X-Auth-Token': token }
        response = requests.get(url, headers=headers)
        matches = response.json()
        return matches


cup = WorldCupApi()
token = open("token").read()
matches = cup.get_matches(token=token)
