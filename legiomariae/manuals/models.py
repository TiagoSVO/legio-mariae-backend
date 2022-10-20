from django.db import models

from meetings.models import Meeting


class ManualReading(models.Model):
    page = models.IntegerField(verbose_name='Página', blank=True, null=True)
    chapter = models.CharField(max_length=7, verbose_name='Capítulo', blank=True, null=True)
    item = models.CharField(max_length=255, verbose_name='Item', blank=True, null=True)
    theme = models.CharField(max_length=255, verbose_name='Tema', blank=True, null=True)
    number_people_comented = models.IntegerField(verbose_name='Número de Pessoas que Comentaram', blank=True, null=True)
    meeting = models.OneToOneField(Meeting, on_delete=models.CASCADE, verbose_name='Reunião')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Leitura do Manual"
        verbose_name_plural = "Leituras dos Manuais"

    def __str__(self):
        return f'Página {self.page} | Capítulo {self.chapter} | Item {self.item} | Theme {self.theme}'


class ManualReadedBy(models.Model):
    person_name = models.CharField(max_length=255, verbose_name='Nome da Pessoa')
    manual_reading = models.ForeignKey(ManualReading, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Manual lido por"
        verbose_name_plural = "Manuais lidos por"

    def __str__(self):
        return f'{self.person_name}'
