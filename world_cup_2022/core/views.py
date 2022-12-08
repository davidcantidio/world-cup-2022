from django.shortcuts import render
from django.http import HttpResponse
from getmatches import *


cup = WorldCupApi()
token = open("token").read()
matches = cup.get_matches(token=token)

# Create your views here.
def get_matches(request):
    matches = get_matches()
    return render(request, 'base.html' )