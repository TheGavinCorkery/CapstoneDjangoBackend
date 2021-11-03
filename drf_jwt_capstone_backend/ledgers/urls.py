from django.urls import path
from ledgers import views

urlpatterns = [
    #Get all ledgers, from all users
    path('all/', views.get_all_ledgers),
    path('', views.user_ledger),
]