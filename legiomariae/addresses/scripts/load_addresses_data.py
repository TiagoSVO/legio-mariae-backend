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
        print(f'{country["id"]} - País:{country["name"]}')

    print('Fim da primeira parte')
    if Country.objects.filter(id=31).exists():
        print(f'Este país já se encontra cadastrado no sistema com o id {country["id"]}!')
    else:
        print('Verificando país...')
        if brazil:
            with transaction.atomic():
                id = brazil["id"]
                name = brazil["name"]
                acronym = brazil["iso3"]
                code = brazil["numeric_code"]
                phone_code = brazil["phone_code"]

                new_country = Country(id=id, name=name,
                                      acronym=acronym, code=code,
                                      phone_code=phone_code)

                new_country.save()

    jsonfile.close()
