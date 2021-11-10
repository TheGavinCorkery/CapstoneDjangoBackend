from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.serializers import Serializer
from .models import Goal
from .serializers import GoalSerializer
from django.contrib.auth import get_user_model
from django.db.models import Q, Sum, F, Count

User = get_user_model()

# Create your views here.
@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_goals(request):
    if request.method == 'POST':
        serializer = GoalSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        transactions = Goal.objects.filter(user_id=request.user.id)
        serializer = GoalSerializer(transactions, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)