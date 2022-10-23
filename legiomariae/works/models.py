from django.db import models

from meetings.models import Meeting
from members.models import MemberFiliation


class Work(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome do Trabalho')
    description = models.TextField(verbose_name='Descrição', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Trabalho"
        verbose_name_plural = "Trabalhos"

    def __str__(self):
        return f'{self.name}'


class ParticipationType(models.Model):
    code = models.CharField(max_length=3, verbose_name='Código do Tipo de Participação')
    name = models.CharField(max_length=30, verbose_name='Nome do Tipo de Participação')
    description = models.TextField(verbose_name="Descrição", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Participação"
        verbose_name_plural = "Participações"

    def __str__(self):
        return f'{self.code} - {self.name}'


class WorkReportStatus(models.Model):
    code = models.CharField(max_length=3, verbose_name='Código do Status do Relatório do Trabalho')
    name = models.CharField(max_length=30, verbose_name='Nome do Status do Relatório do Trabalho')
    description = models.TextField(verbose_name="Descrição", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Status do Relatório do Trabalho"
        verbose_name_plural = "Status dos Relatórios dos Trabalhos"

    def __str__(self):
        return f'{self.code} - {self.name}'


class WorkSheet(models.Model):
    start_date = models.DateField(verbose_name='Data de Início')
    end_date = models.DateField(verbose_name='Data de Fim')
    meeting = models.OneToOneField(Meeting, on_delete=models.CASCADE, verbose_name='Reunião')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Folha de Trabalho | Trabalhos da Semana"
        verbose_name_plural = "Folhas de Trabalhos | Trabalhos das Semanas"

    def __str__(self):
        return f'{self.meeting.get_formatted_label}'


class WorkSheetItem(models.Model):
    work_sheet = models.ForeignKey(WorkSheet, on_delete=models.CASCADE, verbose_name='Folha de Trabalhos')
    work = models.ForeignKey(Work, on_delete=models.CASCADE, verbose_name='Trabalho')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Item da Folha de Trabalho"
        verbose_name_plural = "Itens das Folhas de Trabalhos"

        constraints = [
            models.UniqueConstraint(fields=['work_sheet', 'work'],
                                    name='unique_work_in_work_sheet'),
        ]

    def __str__(self):
        return f'{self.work.name}'


class WorkSheetItemMemberFiliation(models.Model):
    work_sheet_item = models.ForeignKey(WorkSheetItem, on_delete=models.CASCADE,
                                        verbose_name='Item da Folha de Trabalhos')
    member_filiation = models.ForeignKey(MemberFiliation, on_delete=models.CASCADE, verbose_name='Membro')
    participation_type = models.ForeignKey(ParticipationType, on_delete=models.SET_NULL,
                                           verbose_name='Tipo de Participação', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Membro no Item da Folha de Trabalho"
        verbose_name_plural = "Membros nos Itens das Folhas de Trabalhos"

        constraints = [
            models.UniqueConstraint(fields=['work_sheet_item', 'member_filiation'],
                                    name='unique_member_filiation_in_work_sheet_item'),
        ]

    def __str__(self):
        return f'{self.participation_type.name} - {self.member_filiation.get_member_name} | Trabalho: {self.work_sheet_item.work.name}'


class WorkReport(models.Model):
    duration_time = models.DurationField(verbose_name='Duração')
    contacts_number = models.IntegerField(verbose_name='Contatos')
    report_description = models.TextField(verbose_name='Relatório do Trabalho')
    work_sheet_item = models.OneToOneField(WorkSheetItem, on_delete=models.CASCADE,
                                           verbose_name='Item da Folha de Trabalhos')
    work_report_status = models.ForeignKey(WorkReportStatus, on_delete=models.SET_NULL, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Relatório de Trabalho"
        verbose_name_plural = "Relatórios de Trabalhos"

    def __str__(self):
        return f'Trabalho: {self.work_sheet_item.work.name} | '

    @property
    def get_organization_name(self):
        return f'{self.work_sheet_item.work_sheet.meeting.organization_name}'

    @property
    def get_work_sheet_formatted(self):
        return f'{self.work_sheet_item.work_sheet.start_date} à {self.work_sheet_item.work_sheet.end_date}'
