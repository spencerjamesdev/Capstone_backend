from django.shortcuts import render
from .models import Reminder
from .serializers import ReminderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class ReminderList(APIView):

    def get(self, request):
        reminder = Reminder.objects.all()
        serializer = ReminderSerializer(reminder, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)