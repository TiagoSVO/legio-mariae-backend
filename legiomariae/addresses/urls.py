from django.urls import path
from .views import states_from_country, cities_from_state

urlpatterns = [
    path('states_country_json/<int:country_id>', states_from_country, name='states_from_country_json'),
    path('cities_state_json/<int:state_id>', cities_from_state, name='cities_from_state_json'),
]