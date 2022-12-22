from django.shortcuts import render

# Create your views here.
from django.utils import timezone

import requests
from pprint import pprint
from matches.models import  Match, Competition
from datetime import date, datetime, timedelta
from .forms import CompetitionForm


# timezone = pytz.timezone('America/Sao_Paulo')
today = date.today()       
tomorrow = today + timedelta(days=+1)
yesterday = today + timedelta(days=-1)

# Create your views here
def matches(request):
    select_competition_dropdown = CompetitionForm
    if request.method == "POST":
        selected_competition = request.POST['competitions']
        all_matches =  Match.objects.filter(competition__id=selected_competition).order_by('-utcDateTimeString')

        context = {
            'select_competition_dropdown' : select_competition_dropdown,
            'all_matches' : all_matches,        
        }
        this_competition = Competition.objects.get(pk=selected_competition)
        this_competition.lastly_accessed = datetime.now() 
        this_competition.save()
        
        print (f'lA: {this_competition.lastly_accessed}')
        return render(request, 'base.html', context=context)
        
    else:
        all_matches =  Match.objects.filter(competition__id='2000').order_by('-utcDateTimeString')

        context = {
            'select_competition_dropdown' : select_competition_dropdown,
            'all_matches' : all_matches,        
        }
        return render(request, 'base.html', context=context)



# 'all_matches':all_matches, 'today_matches':today_matches, 'future_matches':future_matches, 'past_matches':past_matches}ww