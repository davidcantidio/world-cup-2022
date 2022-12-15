from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_today_matches, name='get_today_matches'),
    

]