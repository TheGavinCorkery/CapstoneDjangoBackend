from django.urls import path
from transactions import views

urlpatterns = [
    #Get all transactions, from all users
    path('all/', views.get_all_transactions),
    #Get all transactions, from specific user
    path('', views.user_transactions),
    #Get all transactions for a users category
    path('category/all/', views.user_category_transactions)
]