from django.urls import path
from reminders import views

urlpatterns = [
    path('all/', views.get_all_reminders),
    path('', views.user_reminders)
]