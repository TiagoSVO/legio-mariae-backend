from django.http import JsonResponse
from .models import State, City


def states_from_country(request, country_id):
    states = []
    if not country_id == 0:
        states = State.serialize_fields_for_select_by_country(country_id)

    return JsonResponse(states, safe=False)


def cities_from_state(request, state_id):
    cities = []
    if not state_id == 0:
        cities = City.serialize_fields_for_select_by_state(state_id)

    return JsonResponse(cities, safe=False)