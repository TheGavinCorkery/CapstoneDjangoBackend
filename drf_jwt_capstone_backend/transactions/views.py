from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Transaction
from .serializers import TransactionSerializer, CategoryListSerializer
from django.contrib.auth import get_user_model
from django.db.models import Q, Sum

User = get_user_model()

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_transactions(request):
    transactions = Transaction.objects.all()
    serializer = TransactionSerializer(transactions, many = True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_transactions(request):

    if request.method == 'POST':
        serializer = TransactionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        transactions = Transaction.objects.filter(user_id=request.user.id)
        serializer = TransactionSerializer(transactions, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_category_transactions(request):
    transactions = Transaction.objects.filter(Q(ledger_id=request.data['ledger']) & Q(category = request.data['category']) & Q(user_id=request.user.id))
    serializer = TransactionSerializer(transactions, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_ledger_transactions(request):
    transactions = Transaction.objects.filter(Q(ledger_id=request.data['ledger']) & Q(user_id=request.user.id))
    serializer = TransactionSerializer(transactions, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_transaction(request):
    transaction = Transaction.objects.get(Q(id = request.data['id']))
    transaction.date = request.data['date']
    transaction.place = request.data['place']
    transaction.total = request.data['total']
    transaction.description = request.data['description']
    transaction.category = request.data['category']
    transaction.save()
    return Response(status = status.HTTP_202_ACCEPTED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_categories_totals(request):
    categories = Transaction.objects.filter(Q(user_id = request.user.id))
    user_category_by_ledger = categories.values('ledger_id', 'category').annotate(total = Sum('total'))
    serializer = CategoryListSerializer(user_category_by_ledger, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)