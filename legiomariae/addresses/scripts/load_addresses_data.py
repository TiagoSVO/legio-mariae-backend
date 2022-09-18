import json
from django.db import transaction

from ..models import Country, State, City


def run():
    jsonfile = open('addresses/scripts/countries_states_cities.json')

    data = json.load(jsonfile)

    brazil = None

    for country in data:
        if country["id"] == 31:
            brazil = country

    if Country.objects.filter(id=31).exists():
        print(f'Este país já se encontra cadastrado no sistema com o id {31}!')
    else:
        print('Verificando país...')
        if brazil:
            # set_country(brazil)
            set_country_states_cities(brazil)

    jsonfile.close()


def set_country(country):
    with transaction.atomic():
        id = country["id"]
        name = country["name"]
        acronym = country["iso3"]
        code = country["numeric_code"]
        phone_code = country["phone_code"]

        new_country = Country(id=id, name=name,
                              acronym=acronym, code=code,
                              phone_code=phone_code)

        new_country.save()
        return new_country


def set_state(country_id, state):
    with transaction.atomic():
        id = state["id"]
        name = state["name"]
        acronym = state["state_code"]

        new_state = State(id=id,
                          name=name,
                          acronym=acronym,
                          country=country_id)

        new_state.save()
        return new_state


def set_city(state_id, city):
    with transaction.atomic():
        id = city["id"]
        name = city["name"]

        new_city = City(id=id,
                        name=name,
                        state=state_id)

        new_city.save()
        return new_city


def set_country_states_cities(country):
    with transaction.atomic():
        new_country = set_country(country)

        states = country["states"]
        for state in states:
            new_state = set_state(new_country, state)

            cities = state["cities"]
            for city in cities:
                set_city(new_state, city)
