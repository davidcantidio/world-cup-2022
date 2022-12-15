from django.shortcuts import render
from django.utils import timezone

import requests
from pprint import pprint
from core.models import Match
from datetime import date, datetime, timedelta
import pytz

timezone = pytz.timezone('America/Sao_Paulo')
today = date.today()       
tomorrow = today + timedelta(days=+1)
yesterday = today + timedelta(days=-1)

# Create your views here
def get_today_matches(request):
    if request.method == "GET":
        headers = {'X-Auth-Token': '0cfc9017d2e64feabaac965138ad845c'}
        url = 'http://api.football-data.org/v4/competitions/2000/matches'
        response = requests.get(url, headers=headers)
        data = response.json()
        
        for d in data['matches']:            
            date_time = datetime.strptime(d['utcDate'], '%Y-%m-%dT%H:%M:%SZ')
            aware_datetime = pytz.utc.localize(date_time)
            date = aware_datetime.date()

            matches = Match(
                id = d['id'],
                utcDateTime = aware_datetime,
                utcDate = date,
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
                comptetition_name = d['competition']['name'],
                competition_emblem = d['competition']['emblem'],
                group = d['group'],
                match_duration = d['score']['duration'],
                score_fullTime_awayTeam = d['score']['fullTime']['away'],
                score_fullTime_homeTeam = d['score']['fullTime']['home'],
            )
            matches.save()

        all_matches =  Match.objects.all().order_by('-utcDate')
        for m in all_matches:
            if not m.awayTeam_name and not m.homeTeam_name:
                m.awayTeam_name = "TBD"
                m.awayTeam_crest_url = "https://www.svgrepo.com/show/91549/question-mark-inside-a-circle.svg"
                m.homeTeam_name = "TBD"     
                m.homeTeam_crest_url = "https://www.svgrepo.com/show/91549/question-mark-inside-a-circle.svg"
                
        today_matches = all_matches.filter(utcDate = today)
        past_matches = all_matches.filter(utcDate__lte = yesterday)
        future_matches = all_matches.filter(utcDate__gte = tomorrow)
        for m in future_matches:
            if not m.score_fullTime_awayTeam:
                m.score_fullTime_homeTeam = ""
                m.score_fullTime_awayTeam = ""

        
        return render(request, 'base.html', {'all_matches':all_matches, 'today_matches':today_matches, 'future_matches':future_matches, 'past_matches':past_matches})

