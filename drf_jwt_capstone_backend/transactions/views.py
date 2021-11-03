from django.shortcuts import render
from rest_framework import status
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Transaction
from .serializers import TransactionSerializer
from django.contrib.auth import get_user_model

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
    transactions = Transaction.object.filter(ledger_id=request.data.ledger_id, category = request.data.category)
    serializer = TransactionSerializer(transactions, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)