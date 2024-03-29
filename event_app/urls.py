# event_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('segments/', views.segments, name='segments'),
    path('soccebot-registration/', views.soccerbot_registration, name='soccer'),
    path('line-follower-robot-registration/',
         views.linefollow_registration, name='line-follow'),
    path('project-showcasing-registration/',
         views.robo_race_registration, name='robo-racing'),
    path('prompt-engineering-registration/',
         views.chatbot_registration, name='chatbot'),
    path('idea-competetion-registration/',
         views.idea_gen_registration, name='idea-gen'),
    path('registration-complete/', views.registration_complete,
         name='reg-complete'),  # Add this line
    path('web-dev-team/', views.web_dev_team,
         name='web-dev-team'),  # Add this line
]
