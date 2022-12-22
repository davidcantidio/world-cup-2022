from django.db import models
from django.utils import timezone
from datetime import date, datetime, timedelta
import pytz

# Create your models here.
class Competition(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    area_code = models.CharField(max_length=3, null=True)
    area_flag = models.CharField(max_length=300, null=True)
    area_name = models.CharField(max_length=30, null=True)
    
    start_date = models.DateField(max_length=10, null=True)
    end_date = models.DateField(max_length=10, null=True)
    emblem = models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=30, null=True)
    plan = models.CharField(max_length=30, null=True)
    competition_type = models.CharField(max_length=30, null=True)
    lastly_accessed = models.DateTimeField(default=datetime.now())

    class Meta:
        ordering = ('-lastly_accessed',)

    def __str__(self):
        return self.name
  


class Match(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, null=True)
    id = models.CharField(max_length=50, primary_key=True)
    utcDateTimeString = models.CharField(max_length=20, null=True)
    winner = models.CharField(max_length=90, null=True, default='TBD')
    stage = models.CharField(max_length=40, null=True)
    status = models.CharField(max_length=20, null=True)
    awayTeam_name = models.CharField(max_length=40, null=True, default='TBD')
    awayTeam_shortName = models.CharField(max_length=40, null=True, default='TBD')
    awayTeam_tla = models.CharField(max_length=4, null=True, default='TBD')
    awayTeam_crest_url = models.CharField(max_length=200, null=True, default='https://www.svgrepo.com/show/91549/question-mark-inside-a-circle.svg')

    homeTeam_name = models.CharField(max_length=40, null=True, default='TBD')
    homeTeam_shortName = models.CharField(max_length=40, null=True)
    homeTeam_tla = models.CharField(max_length=4, null=True)
    homeTeam_crest_url = models.CharField(max_length=200, null=True, default='https://www.svgrepo.com/show/91549/question-mark-inside-a-circle.svg')
    group = models.CharField(max_length=20, null=True)
    match_duration = models.CharField(max_length=30, null=True)
    score_fullTime_awayTeam = models.IntegerField(null=True, default='0')
    score_fullTime_homeTeam = models.IntegerField(null=True, default='0')

    class Meta:
        ordering = ('-utcDateTimeString',)

    def __str__(self):
        label = f'{self.homeTeam_tla} vs {self.awayTeam_tla}'
        return label
  
    @property 
    def aware_date(self):
        date_time = datetime.strptime(self.utcDateTimeString, '%Y-%m-%dT%H:%M:%SZ')
        aware_datetime = pytz.utc.localize(date_time)
        
        return aware_datetime.date()


    @property
    def is_in_past(self):
        return self.aware_date < datetime.today().date()
    
    @property
    def is_today(self):
        return self.aware_date == datetime.today().date()


    @property
    def is_in_future(self):
        return self.aware_date > datetime.today().date()
    
