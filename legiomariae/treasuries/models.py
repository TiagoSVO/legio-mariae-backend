from django.db import models
from djmoney.models.fields import MoneyField, get_currency

from meetings.models import Meeting


class TreasuryReport(models.Model):
    date = models.DateField(verbose_name='Data')
    previous_balance = MoneyField(max_digits=20, decimal_places=2, default_currency='BRL', verbose_name='Saldo Anterior')
    collection_day = MoneyField(max_digits=10, decimal_places=2, default_currency='BRL', verbose_name='Coleta do Dia')
    cash_balance = MoneyField(max_digits=20, decimal_places=2, default_currency='BRL', verbose_name='Saldo do Dia')
    meeting = models.ForeignKey(Meeting, on_delete=models.SET_NULL, verbose_name='Reunião', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Relatório da Tesouraria"
        verbose_name_plural = "Relatórios das Tesourarias"

        constraints = [
            models.UniqueConstraint(fields=['meeting', 'date'], name='unique_report_for_meeting'),
        ]

    def __str__(self):
        return f'{self.get_organization}'

    @property
    def get_organization(self):
        return f'Relatório da Tesouraria: {self.date} | {self.meeting.organization.our_blessed_lady_title.name}'


class Expense(models.Model):
    description = models.CharField(max_length=255, verbose_name='Descrição da Despesa')
    value = MoneyField(max_digits=20, decimal_places=2, default_currency='BRL', verbose_name='Valor')
    treasury_report = models.ForeignKey(TreasuryReport, on_delete=models.CASCADE, verbose_name='Relatório da Tesouraria')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Despesa"
        verbose_name_plural = "Despesas"

    def __str__(self):
        return f'{self.description}: {self.value}'
