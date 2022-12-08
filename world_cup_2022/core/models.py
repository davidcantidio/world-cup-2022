from django.db import models

# Create your models here.
class Match(models.Model):
    startDate = models.CharField(max_length=50)
    winner = models.CharField(max_length=90)
    stage = models.CharField(max_length=40)
    status = models.CharField(max_length=20)
    awayTeam_name = models.CharField(max_length=40)
    awayTeam_shortName = models.CharField(max_length=40)
    awayTeam_tla = models.CharField(max_length=4)
    awayTeam_crest_url = models.CharField(max_length=200)
    homeTeam_name = models.CharField(max_length=40)
    homeTeam_shortName = models.CharField(max_length=40)
    homeTeam_tla = models.CharField(max_length=4)
    homeTeam_crest_url = models.CharField(max_length=200)
    comptetition_name = models.CharField(max_length=40)
    competition_emblem = models.CharField(max_length=30)
    group = models.CharField(max_length=20)
    match_duration = models.CharField(max_length=30)
    score_fullTime_awayTeam = models.IntegerField()
    score_fullTime_homeTeam = models.IntegerField()

def __str__(self):
    label = f'{self.homeTeam_tla} vs {self.awayTeam_tla}'
    return label