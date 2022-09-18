import json

from addresses.models import Country, State, City


def run():
    jsonfile = open('countries_states_cities.json')

    data = json.load(jsonfile)

    for country in data:
        print(f'{country["id"]} - País:{country["name"]}')

    jsonfile.close()
