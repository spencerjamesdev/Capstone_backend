from django.urls import path
from . import views

urlpatterns = [
    path('reminders/', views.ReminderList.as_view()),
]