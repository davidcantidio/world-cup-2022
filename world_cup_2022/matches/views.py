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

        #set timestamp for this competition as lastly accessed
        this_competition = Competition.objects.get(pk=selected_competition)
        this_competition.lastly_accessed = datetime.now() 
        this_competition.save()

    else: 
        selected_competition = '2000'
    
    all_matches =  Match.objects.filter(competition__id=selected_competition).order_by('-utcDateTimeString')
    past_matches = ([i for i in all_matches if i.is_in_past])
    today_matches = ([i for i in all_matches if i.is_today])
    future_matches = ([i for i in all_matches if i.is_in_future])
    
    context = {
        'select_competition_dropdown' : select_competition_dropdown,
        'all_matches' : all_matches,  
        'today_matches' : today_matches,
        'future_matches' : future_matches,
        'past_matches' : past_matches
    }

    return render(request, 'matches.html', context=context)
        
    