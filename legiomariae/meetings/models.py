from django.db import models

from utils.utils import months_names
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
        return self.get_formatted_label

    @property
    def organization_type_name(self):
        return f'{self.organization.organization_type.name}'

    @property
    def organization_name(self):
        return f'{self.organization.our_blessed_lady_title.name}'

    @property
    def get_formatted_label(self):
        return f'Reunião do dia {self.date} | {self.organization_type_name} {self.organization_name}'

    @property
    def date_in_full(self):
        day = self.date.strftime('%d')
        month = months_names['pt_BR'][self.date.strftime('%m')]
        year = self.date.strftime('%Y')

        if day == '01':
            final_text = f'No primeiro dia '
        else:
            final_text = f'Aos {day} dias '

        final_text += f'do mês de {month} de {year}'

        return final_text

    @property
    def start_at_in_full(self):
        hour = self.start_at.strftime('%H')
        minute = self.start_at.strftime('%M')
        return f'{hour}h{minute}'


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


class MeetingMinute(models.Model):
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

    @property
    def build_text_minute_title(self):
        return f'Ata {self.minute_number}'

    @property
    def built_text_minute_introduction(self):
        meeting = self.meeting
        address = meeting.organization.addresses.all()[0]
        organization = meeting.organization
        preposition_inital_prayer = 'com' if meeting.initial_prayer else 'sem'
        rosary_prayer = 'seguidas do' if meeting.rosary_prayer else 'sem o'

        final_text = f'{meeting.date_in_full}, às {meeting.start_at_in_full}, {meeting.place_address}, ' \
                     f'{address.state.name} - {address.state.acronym}, ' \
                     f'iniciou-se mais uma reunião semanal do ' \
                     f'{organization.organization_type.name.lower()} {organization.full_name}, ' \
                     f'sob a proteção de Nossa Senhora, ' \
                     f'{preposition_inital_prayer} as orações iniciais da tessera ' \
                     f'{rosary_prayer} santo terço. '

        return final_text

    def build_text_for_spiritual_read(self):
        meeting = self.meeting
        spiritual_read = meeting.spiritual_read

        return f'A leitura espiritual foi retirada de {spiritual_read}.'

    def create_meeting_minute(self, meeting_id = None):
        meeting_id = meeting_id or self.meeting
        if not meeting_id:
            raise ValueError('The meeting id is missing!')

        meeting = Meeting.objects.filter(id=meeting_id)[0]
        meeting_minute = meeting.meetingminute

        data = {
            'meeting': meeting,
            'meeting_minute': meeting_minute
        }

        return self.build_minute_text(data)

    def build_minute_text(self, data=None):
        if data is None:
            raise ValueError('Data to build minute is missing!')
        meeting_minute = data['meeting_minute']

        minute_text = f'{meeting_minute.build_text_minute_title}\n' \
                      f'{meeting_minute.built_text_minute_introduction} ' \
                      f'meeting_minutef{meeting_minute.build_text_for_spiritual_read} ' \
                      f'Foi feita a leitura da ata 843, assinada pela presidente, ' \
                      f'irmã Mariel com a seguinte observação: ' \
                      f'dentre as despesas no relatório da tesouraria ' \
                      f'também estão inclusos os panfletos de divulgação dos Patrícios. ' \
                      f'À chamada estavam presentes os irmãos: ' \
                      f'Mariel, Mariane, Monique, Daniela, Rodrigo e Tiago. ' \
                      f'Recrutamento: foi feito um convite para membro ativo durante a semana. ' \
                      f'Foi lida a instrução permanente. Prestação de contas do trabalho semanal: ' \
                      f'Divulgação do retiro foi realizado pelos irmãos Mariane, ' \
                      f'Daniela e Rodrigo com 500 contatos e 1h de duração. ' \
                      f'O trabalho foi realizado na missa das 12h de domingo ' \
                      f'e duas pessoas vieram perguntar a respeito. Distribuição dos trabalhos: ' \
                      f'Terço em família para Monique, Visita ao HFA para Rodrigo e Mariane, ' \
                      f'Visita a membro auxiliar para Daniela e Mariel e Yeshua III para Tiago. ' \
                      f'Todos rezaram a Catena Legionis. Allocutio: ' \
                      f'Essa passagem remete ao poder da palavra e o impacto dela na vida das pessoas. ' \
                      f'Palavras são tão fortes que Deus criou o mundo por meio delas e o salvou encarnando ' \
                      f'sua palavra. Que nossa boca não seja um túmulo, mas um berçário que traga vida; ' \
                      f'essas palavras que saem de nós devem vir para transformar positivamente a vida do outro. ' \
                      f'Seguiu-se com a coleta secreta e foi lido o relatório da tesouraria de: ' \
                      f'28/07/2019: saldo $17,00, coleta do dia $83,25 e saldo em caixa $100,25. ' \
                      f'O estudo do manual foi retirado da página 243, capítulo 37, item 7 com o tema ' \
                      f'“Obras a favor da juventude: uma fórmula legionária para a juventude” e foi comentado ' \
                      f'por três irmãos. Avisos e outros assuntos: ' \
                      f'11/08- Dia das vocações matrimoniais; Dia dos pais; ' \
                      f'12/08- Dia internacional da juventude; ' \
                      f'13/08- Beata Dulce dos Pobres, Início da Semana Nacional da Família; ' \
                      f'15/08- Assunção de Nossa Senhora (indulgência plenária); ' \
                      f'17/08- reunião de régia (14h); 18/08- Dia das vocações religiosas. ' \
                      f'Sem mais nenhum assunto a tratar, rezou-se as orações finais da tessera ' \
                      f'e encerrou-se a reunião às 11h39min.'

        return minute_text


class MeetingMinuteReaded(models.Model):
    observations = models.TextField(verbose_name='Observações', null=True, blank=True)
    meeting = models.ForeignKey(Meeting, verbose_name='Reunião em que foi lida', on_delete=models.CASCADE, related_name='in_meeting_readed')
    minute = models.ForeignKey(MeetingMinute, verbose_name='Ata Lida', on_delete=models.CASCADE, related_name='minute_readed')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ata Lida de Reunião Anterior"
        verbose_name_plural = "Atas Lida de Reuniões Anteriores"

    def __str__(self):
        return f'Ata lida, número: {self.minute.minute_number}'
