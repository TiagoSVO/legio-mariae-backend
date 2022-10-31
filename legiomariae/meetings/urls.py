from django.urls import path
from .views import generate_minute_meeting

urlpatterns = [
    path('data_minute/<int:meeting_id>', generate_minute_meeting, name='states_from_country_json'),
]
