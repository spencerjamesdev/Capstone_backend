from rest_framework import serializers
from .models import Reminder


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ['id', 'name', 'description', 'recurrence', 'day', 'user_id', 'is_completed']