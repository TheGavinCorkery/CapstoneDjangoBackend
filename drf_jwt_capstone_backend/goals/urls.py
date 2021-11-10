from django.urls import path
from goals import views

urlpatterns = [
    #Get all user goals and post a new goal
    path('', views.user_goals),
]
