import requests
from pprint import pprint

response = requests.get('http://api.football-data.org/v4/competitions/')
pprint(response.json())