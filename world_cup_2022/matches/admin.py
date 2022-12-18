from django.contrib import admin

# Register your models here.
from .models import Match, Competition
admin.site.register(Match)
admin.site.register(Competition)