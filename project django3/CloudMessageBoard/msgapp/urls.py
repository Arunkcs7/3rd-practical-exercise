from django.urls import path
from .views import submit_message, get_messages

urlpatterns = [
    path('submit/', submit_message, name='submit_message'),
    path('get/<str:sender_name>/', get_messages, name='get_messages'),
]
