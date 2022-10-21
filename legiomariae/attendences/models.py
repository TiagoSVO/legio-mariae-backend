from django.db import models

from meetings.models import Meeting
from members.models import MemberFiliation


class AttendenceSheet(models.Model):
    total_invites = models.IntegerField(verbose_name='Total de Convites', default=0)
    total_recruitments = models.IntegerField(verbose_name='Total de Recrutamentos', default=0)
    meeting = models.OneToOneField(Meeting, verbose_name='Reunião', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Folha de Chamada"
        verbose_name_plural = "Folhas de Chamadas"

    def __str__(self):
        return f'Folha de Chamada | {self.meeting}'


class AttendenceSheetMemberStatus(models.Model):
    code = models.CharField(max_length=3, verbose_name='Código')
    name = models.CharField(max_length=255, verbose_name='Nome')
    description = models.TextField(verbose_name='Descrição', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Status do Membro na Chamada"
        verbose_name_plural = "Status dos Membros nas Chamadas"

    def __str__(self):
        return f'{self.member}'


class AttendenceSheetMember(models.Model):
    invites_number = models.IntegerField(verbose_name='Número de Convites', default=0)
    recruitments_number = models.IntegerField(verbose_name='Número de Recrutamentos', default=0)
    member_filiation = models.ForeignKey(MemberFiliation, on_delete=models.CASCADE)
    attendence_sheet = models.ForeignKey(AttendenceSheet, on_delete=models.CASCADE)
    status = models.ForeignKey(AttendenceSheetMemberStatus, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Membro na Chamada"
        verbose_name_plural = "Membros nas Chamadas"

        constraints = [
            models.UniqueConstraint(fields=['member_filiation', 'attendence_sheet'],
                                    name='unique_memberfiliation_in_attendencesheet'),
        ]

    def __str__(self):
        return f'{self.member_filiation}'
