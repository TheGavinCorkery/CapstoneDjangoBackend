from django.urls import path
from ledgers import views

urlpatterns = [
    #Get all ledgers, from all users
    path('all/', views.get_all_ledgers),
    #Get ledgers from user, post new ledger for a user
    path('', views.user_ledger),
]