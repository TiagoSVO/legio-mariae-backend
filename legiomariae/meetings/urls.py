from django.urls import path
from .views import generate_meeting_minute

urlpatterns = [
    path('data_minute/<int:meeting_id>', generate_meeting_minute, name='states_from_country_json'),
]
