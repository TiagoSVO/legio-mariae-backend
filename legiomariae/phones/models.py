from django.db import models
from addresses.models import Country


def phone_code_formatted(country):
    return country.phone_code, f'+{country.phone_code} | {country.name}'


CONTRIES_CODES = tuple(map(phone_code_formatted, Country.objects.all()))


class Phone(models.Model):
    country_code = models.CharField(max_length=3, choices=CONTRIES_CODES, default='001',
                                    null=True, blank=True,
                                    verbose_name='Código do País')
    prefix = models.CharField(max_length=3)
    number = models.CharField(max_length=9)

    class Meta:
        abstract = True
        verbose_name = "Telefone"
        verbose_name_plural = "Telefones"

    def __str__(self):
        return f'{self.number_formatted}'

    @property
    def number_formatted(self):
        number = f'{self.number[0]}.{self.number[1:5]}-{self.number[5:]}' if len(
            self.number) > 8 else f'{self.number[0:4]}-{self.number[4:]}'
        return f'({self.prefix}) {number}'
