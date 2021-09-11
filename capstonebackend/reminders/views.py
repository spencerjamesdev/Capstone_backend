from django.http.response import Http404
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


class ReminderDetail(APIView):

    def get_object(self, pk):
        try:
            return Reminder.objects.get(pk=pk)
        except Reminder.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        reminder = self.get_object(pk)
        serializer = ReminderSerializer(reminder)
        return Response(serializer.data)

    def put(self, request, pk):
        reminder = self.get_object(pk)
        serializer = ReminderSerializer(reminder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        reminder = self.get_object(pk)
        reminder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)