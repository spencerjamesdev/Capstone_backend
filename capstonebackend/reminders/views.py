from django.http.response import Http404
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Reminder
from .serializers import ReminderSerializer
from django.contrib.auth.models import User


# Create your views here

@api_view(['GET'])
@permission_classes([AllowAny])

# Gets all reminders from every user, probably wont be utalized
def get_all_reminders(request):
    reminders = Reminder.objects.all()
    serializer = ReminderSerializer(reminders, many=True)
    return Response(serializer.data)


    
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])

#Only available if the user is logged in
def user_reminders(request):
    if request.method == 'GET':
        reminder = Reminder.objects.filter(user_id=request.user.id)
        serializer = ReminderSerializer(reminder, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
@permission_classes([AllowAny])   
def delete_user_reminders(request, reminder_id):   
    reminder = Reminder.objects.filter(pk = reminder_id)
    reminder.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_reminder(request, pk):
    
    try:
        reminder = Reminder.objects.get(pk=pk)
    except Reminder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    serializer = ReminderSerializer(reminder, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)