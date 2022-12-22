import os 
PROJECT_NAME = 'world_cup_2022'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '%s.settings' %PROJECT_NAME)

import django
django.setup()

from matches.models import Competition, Match
import requests
from pprint import pprint
import json
from datetime import datetime, timedelta

today = datetime.now().date()
dateFrom = today + timedelta(days=0)
dateFrom = dateFrom.strftime("%Y-%m-%d")

dateTo = today + timedelta(days=10)
dateTo = dateTo.strftime("%Y-%m-%d")


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

# def gen_competition_ids():
    
#     for c in competitions: 
#         comp_list.append(c.id)
#     return comp_list


def get_matches():
    competitions = Competition.objects.all()

    comp_list =[c.id for c in competitions]
    headers = {'X-Auth-Token': '0cfc9017d2e64feabaac965138ad845c'}
    matches_url = 'http://api.football-data.org/v4/matches'
    matches_url += "?competitions=" + ",".join(comp_list)
    matches_url += "&dateFrom=" + dateFrom
    matches_url += "&dateTo=" + dateTo
    # pprint(matches_url)
    response = requests.get(matches_url, headers=headers) 
    matches_data = response.json() 
    pprint(matches_data)
    if matches_data.get('matches'):
        comp_queryset = Competition.objects.all()
        for d in matches_data.get('matches'):    
            for c in comp_queryset:
                if d['competition']['id'] == c.id:

                    matches = Match(
                        competition = c,
                        id = d['id'],
                        utcDateTimeString = d['utcDate'],
                        winner = d['score']['winner'],
                        stage = d['stage'],
                        status = d['status'],
                        awayTeam_name = d['awayTeam']['name'],
                        awayTeam_shortName = d['awayTeam']['shortName'],
                        awayTeam_tla = d['awayTeam']['tla'],
                        awayTeam_crest_url = d['awayTeam']['crest'],
                        homeTeam_name = d['homeTeam']['name'],
                        homeTeam_shortName = d['homeTeam']['shortName'],
                        homeTeam_tla = d['homeTeam']['tla'],
                        homeTeam_crest_url = d['homeTeam']['crest'],
                        group = d['group'],
                        match_duration = d['score']['duration'],
                        score_fullTime_awayTeam = d['score']['fullTime']['away'],
                        score_fullTime_homeTeam = d['score']['fullTime']['home'],
                        )
                    matches.save()
            
if __name__ == '__main__':
    django.setup()
    # get_matches()
    for m in Match.objects.all():
        print(m.is_in_past)