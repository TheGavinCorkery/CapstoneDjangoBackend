from django.urls import path
from goals import views

urlpatterns = [
    #Get all user goals and post a new goal
    path('', views.user_goals),
    #Get goal by user, category, and ledger
    path('category/', views.user_goal_category_ledger),
]
