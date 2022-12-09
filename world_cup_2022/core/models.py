from django.db import models
from django.utils import timezone

# Create your models here.
class Match(models.Model):
    utcDate = models.CharField(max_length=50, null=True)
    startDate = models.CharField(max_length=50)
    winner = models.CharField(max_length=90, null=True)
    stage = models.CharField(max_length=40, null=True)
    status = models.CharField(max_length=20, null=True)
    awayTeam_score_color = models.CharField(max_length=20, null=True)
    awayTeam_name = models.CharField(max_length=40, null=True)
    awayTeam_shortName = models.CharField(max_length=40, null=True)
    awayTeam_tla = models.CharField(max_length=4, null=True)
    awayTeam_crest_url = models.CharField(max_length=200, null=True)
    homeTeam_score_color = models.CharField(max_length=20, null=True)
    homeTeam_name = models.CharField(max_length=40, null=True)
    homeTeam_shortName = models.CharField(max_length=40, null=True)
    homeTeam_tla = models.CharField(max_length=4, null=True)
    homeTeam_crest_url = models.CharField(max_length=200, null=True)
    comptetition_name = models.CharField(max_length=40, null=True)
    competition_emblem = models.CharField(max_length=30, null=True)
    group = models.CharField(max_length=20, null=True)
    match_duration = models.CharField(max_length=30, null=True)
    score_fullTime_awayTeam = models.IntegerField(null=True)
    score_fullTime_homeTeam = models.IntegerField(null=True)

    class Meta:
        ordering = ('-startDate',)

    def __str__(self):
        label = f'{self.homeTeam_tla} vs {self.awayTeam_tla}'
        return label
    
    @property
    def is_in_past(self):
        return self.startDate < timezone.now()