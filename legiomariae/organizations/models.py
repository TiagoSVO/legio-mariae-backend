from django.db import models


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
