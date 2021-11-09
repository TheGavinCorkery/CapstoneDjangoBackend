from django.urls import path
from transactions import views

urlpatterns = [
    #Get all transactions, from all users
    path('all/', views.get_all_transactions),
    #Get all transactions, from specific user and post a new user transaction
    path('', views.user_transactions),
    #Get all transactions for a users category with ledger
    path('category/all/', views.user_category_transactions),
    #Get all transactions for a users ledger
    path('ledger/all/', views.user_ledger_transactions),
    #Update a users transaction
    path('transaction/edit', views.update_user_transaction),
    #Get users ledgers and categories
    path('ledgers/list', views.get_user_categories_totals),
    #Get users ledgers totals
    path('ledgers/totals', views.get_ledger_totals),
    #Get categories for ledger
    path('ledger/categories', views.ledger_categories)
]