import os 
PROJECT_NAME = 'world_cup_2022'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '%s.settings' %PROJECT_NAME)

import django
django.setup()

from matches.models import Competition
import requests
from pprint import pprint


def competitions():
    headers = {'X-Auth-Token': '0cfc9017d2e64feabaac965138ad845c'}
    competition_url = 'http://api.football-data.org/v4/competitions/'
    response = requests.get(competition_url, headers=headers) 
    competition_data = response.json()

    for c in competition_data.get('competitions'):
        competitions = Competition(
            id = c['id'],
            area_code = c['area']['code'],
            area_flag = c['area']['flag'],
            area_name = c['area']['name'],
            end_date = c['currentSeason']['endDate'],
            start_date = c['currentSeason']['startDate'],
            emblem = c['emblem'],
            name = c['name'],
            plan = c['plan'],
            competition_type = c['type'],
        )       
        competitions.save()
