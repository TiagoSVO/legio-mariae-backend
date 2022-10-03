from django.db import models
from addresses.models import Address


class OrganizationType(models.Model):
    name = models.CharField(max_length=15, verbose_name="Nome")
    description = models.TextField(verbose_name="Descrição")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tipo de Organização"
        verbose_name_plural = "Tipos de Organizações"

    def __str__(self):
        return f'{self.name}'


class OurLadyBlessedTitle(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    celebrate_date = models.DateField(verbose_name="Data de Comemoração", blank=True, null=True)
    description = models.TextField(verbose_name="Descrição", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Título de Nossa Senhora"
        verbose_name_plural = "Títulos de Nossa Senhora"

    def __str__(self):
        return f'{self.name}'


class Organization(models.Model):
    registered_at = models.DateField(verbose_name='Data de Abertura')
    active = models.BooleanField(verbose_name="Ativo", default=True)
    deleted = models.BooleanField(verbose_name="Excluído", default=False)
    organization_type = models.ForeignKey(OrganizationType,
                                          on_delete=models.SET_NULL,
                                          verbose_name="Tipo de Organização",
                                          null=True,
                                          blank=True)
    our_blessed_lady_title = models.ForeignKey(OurLadyBlessedTitle,
                                               on_delete=models.SET_NULL,
                                               verbose_name="Título de Nossa Senhora",
                                               null=True,
                                               blank=True)
    organization_parent = models.ForeignKey('self',
                                            on_delete=models.SET_NULL,
                                            verbose_name="Vinculado à:",
                                            null=True,
                                            blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Organização"
        verbose_name_plural = "Organizações"

    def __str__(self):
        return f'{self.full_name}'

    @property
    def full_name(self):
        return f'{self.our_blessed_lady_title.name}'

    @property
    def linked_church(self):
        address = self.addresses.first()
        return f'{address.linked_church}' if address else '-'



class OrganizationAddress(Address):
    linked_church = models.CharField(max_length=255, verbose_name="Nome da Igreja Vinculada", null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name="Organização", related_name='addresses')

    class Meta:
        verbose_name = "Endereço da Organização"
        verbose_name_plural = "Endereços das Organização"

    def __str__(self):
        return f'{self.get_organization_name} - {self.address_line}'

    @property
    def get_organization_name(self):
        return self.organization.our_blessed_lady_title.name if hasattr(self, 'organization') else ''



