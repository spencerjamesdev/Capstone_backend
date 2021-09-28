
from django.urls import path
from reminders import views

urlpatterns = [
    path('all/', views.get_all_reminders),
    path('', views.user_reminders),
    path('reminder/<int:reminder_id>/', views.delete_user_reminders),
    path('update/<int:pk>/', views.update_reminder)
]