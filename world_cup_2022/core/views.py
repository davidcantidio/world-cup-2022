from django.shortcuts import render
from django.http import HttpResponse
import requests
from pprint import pprint
from core.models import Match

# Create your views here
def get_matches(request):
    if request.method == "GET":
        headers = {'X-Auth-Token': '0cfc9017d2e64feabaac965138ad845c'}
        url = 'http://api.football-data.org/v4/competitions/2000/matches'
        response = requests.get(url, headers=headers)
        data = response.json()
        for d in data['matches']:
            if d['awayTeam']['name']:
                matches = Match(
                    startDate = d['utcDate'],
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
                all_matches = Match.objects.all().order_by('-id')
    return render(request, 'base.html', {'all_matches':all_matches} )