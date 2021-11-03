from django.shortcuts import render
from rest_framework import status
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Ledger
from .serializers import LedgerSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

#Get all ledgers, from all users
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_ledgers(request):
    ledgers = Ledger.objects.all()
    serializer = LedgerSerializer(ledgers, many = True)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_ledger(request):

    if request.method == 'POST':
        serializer = LedgerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        ledgers = Ledger.objects.filter(user_id=request.user.id)
        serializer = LedgerSerializer(ledgers, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
