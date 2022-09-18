from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome do País")
    code = models.CharField(max_length=5, verbose_name="Código do país")
    acronym = models.CharField(max_length=3, verbose_name="Sigla")
    phone_code = models.CharField(max_length=5, verbose_name="Código de Telefone do país")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"

    def __str__(self):
        return f'{self.name}'


class State(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome do Estado")
    phone_code = models.CharField(max_length=5, verbose_name="Código de Telefone do Estado")
    acronym = models.CharField(max_length=3, verbose_name="Sigla")

    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="País")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

    def __str__(self):
        return f'{self.name}'

    @classmethod
    def serialize_fields_for_select_by_country(cls, country_id):
        states_serialized = []
        states_country = cls.objects.filter(country=country_id)

        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        for state in states_country:
            states_serialized.append({'name': state.name, 'value': state.id})

        return states_serialized


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome da Cidade")

    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name='Estado')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = "Cidades"

    def __str__(self):
        return f'${self.name}'

    @classmethod
    def serialize_fields_for_selected_by_state(cls, state_id):
        cities_serialized = []
        cities_state = cls.objects.filter(state=state_id)

        for city in cities_state:
            cities_serialized.append({'title': city.name, 'value': city.id})

        return cities_serialized


class Address(models.Model):
    address_line = models.CharField(max_length=250, verbose_name='Endereço')
    address_number = models.CharField(max_length=10, verbose_name='Número', blank='True', null='True')
    complement = models.CharField(max_length=100, verbose_name='Complemento', blank='True', null='True')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, verbose_name='País', blank=True, null=True)
    zipcode = models.CharField(max_length=8, verbose_name='CEP')
    state = models.ForeignKey(State, on_delete=models.SET_NULL, verbose_name='Estado', blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, verbose_name='Cidade', blank=True, null=True)
    latitude = models.CharField(max_length=9, blank=True, null=True)
    longitude = models.CharField(max_length=10, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return self.complete_address

    @property
    def formatted_zipcode(self):
        zipcode = self.zipcode
        return f'{zipcode[0:2] }.{zipcode[2:2+3]}-{zipcode[5:5+3]}'

    @property
    def complete_address(self):
        return f'{self.address_line} {self.address_number} - {self.city.name}/{self.state.name}'

    @property
    def full_address(self):
        return f'{self.complete_address}, {self.formatted_zipcode}, {self.country.name}'

    @property
    def coordinate_address(self):
        return f'Latitude: {self.latitude} | Longitude: {self.longitude}'

