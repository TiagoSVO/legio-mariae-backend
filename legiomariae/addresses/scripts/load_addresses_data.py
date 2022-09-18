import json
from django.db import transaction

from ..models import Country


def run():
    print('Iniciando')
    jsonfile = open('addresses/scripts/countries_states_cities.json')

    data = json.load(jsonfile)

    brazil = None

    for country in data:
        if country["id"] == 31:
            brazil = country
            
    print('Fim da primeira parte')
    if Country.objects.filter(id=31).exists():
        print(f'Este país já se encontra cadastrado no sistema com o id {31}!')
    else:
        print('Verificando país...')
        if brazil:
            set_country(brazil)

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


def set_state(country_id, state):
    with transaction.atomic():
        id = state["id"]
        name = state["name"]
        acronym = state["state_code"]
        code = state["numeric_code"]
        phone_code = state["phone_code"]

        new_country = Country(id=id, name=name,
                              acronym=acronym, code=code,
                              phone_code=phone_code)

        new_country.save()
