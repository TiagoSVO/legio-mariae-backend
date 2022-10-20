from django.db import models

from members.models import Member
from organizations.models import Organization


class Meeting(models.Model):
    date = models.DateField(verbose_name='Data da Reunião')
    start_at = models.TimeField(verbose_name='Início da Reunião')
    reposition = models.BooleanField(verbose_name='Reposição', default=False)
    place_address = models.CharField(max_length=255, verbose_name='Local da Reunião', blank=True, null=True)
    initial_prayer = models.BooleanField(verbose_name='Orações Iniciais', default=True)
    rosary_prayer = models.BooleanField(verbose_name='Oração do Terço', default=True)
    spiritual_read = models.CharField(max_length=255, verbose_name='Leitura Espiritual', blank=True, null=True)
    standing_instructions_readed = models.BooleanField(verbose_name='Instrução Permanente', default=False)
    catena_prayer = models.BooleanField(verbose_name='Oração da Catena', default=True)
    allocutio = models.TextField(verbose_name='Allocutio', blank=True, null=True)
    announcements = models.TextField(verbose_name='Avisos e Outros Assuntos', blank=True, null=True)
    final_observations = models.TextField(verbose_name='Observações Finais', blank=True, null=True)
    final_prayer = models.BooleanField(verbose_name='Orações Finais', default=True)
    end_at = models.TimeField(verbose_name='Final da Reunião')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name='Organização')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Reunião"
        verbose_name_plural = "Reuniões"

    def __str__(self):
        return f'Reunião do dia {self.date} | {self.organization_type_name} {self.organization_name}'

    @property
    def organization_type_name(self):
        return f'{self.organization.organization_type.name}'

    @property
    def organization_name(self):
        return f'{self.organization.our_blessed_lady_title.name}'


class MeetingOrganizationJoin(models.Model):
    meeting = models.ForeignKey(Meeting, verbose_name='Reunião', on_delete=models.CASCADE)
    organization_guest = models.ForeignKey(Organization, verbose_name='Organização convidada', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Reunião em Conjunto"
        verbose_name_plural = "Reuniões em Conjunto"

    def __str__(self):
        host_organization = self.organization.our_blessed_lady.name
        guest_organization = self.organization_guest.our_blessed_lady.name
        return f'Reunião do dia {self.meeting.date} | Anfitriã: {host_organization} | Convidada: {guest_organization}'


class WelcomeGuest(models.Model):
    guest_name = models.CharField(max_length=255, verbose_name='Nome do Convidado')
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, verbose_name='Reunião')
    welcome_member = models.ForeignKey(Member, on_delete=models.SET_NULL, verbose_name='Membro Acolhedor', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Convidado"
        verbose_name_plural = "Convidados"

    def __str__(self):
        return f'Boas vindas de {self.member.complete_name} a {self.guest_name}'


class MinuteMeeting(models.Model):
    minute_number = models.CharField(max_length=7, verbose_name='Número da Ata', null=True, blank=True)
    description = models.TextField(verbose_name='Descrição completa da Ata', default='### NÃO PREENCHIDA ###')
    meeting = models.OneToOneField(Meeting, verbose_name='Reunião', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ata da Reunião"
        verbose_name_plural = "Atas das Reuniões"

    def __str__(self):
        return f'Ata número: {self.minute_number}'


class MinuteMeetingReaded(models.Model):
    observations = models.TextField(verbose_name='Observações', null=True, blank=True)
    meeting = models.ForeignKey(Meeting, verbose_name='Reunião em que foi lida', on_delete=models.CASCADE, related_name='in_meeting_readed')
    minute = models.ForeignKey(MinuteMeeting, verbose_name='Ata Lida', on_delete=models.CASCADE, related_name='minute_readed')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ata Lida de Reunião Anterior"
        verbose_name_plural = "Atas Lida de Reuniões Anteriores"

    def __str__(self):
        return f'Ata lida, número: {self.minute.minute_number}'
