from django.db import models
from addresses.models import Address
from organizations.models import Organization
from phones.models import Phone


class Member(models.Model):
    complete_name = models.CharField(max_length=255, verbose_name='Nome completo')
    cpf = models.CharField(max_length=11, verbose_name='CPF', null=True, blank=True)
    nickname = models.CharField(max_length=255, verbose_name='Apelido', null=True, blank=True)
    birthday = models.DateField(null=True, blank=True, verbose_name='Data de Nascimento')
    email = models.CharField(max_length=255, verbose_name='E-mail', null=True, blank=True)
    deleted = models.BooleanField(default=False, verbose_name='Excluído?')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Membro"
        verbose_name_plural = "Membros"

    def __str__(self):
        return f'{self.complete_name}'


class MemberAddress(Address):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='Membro')

    class Meta:
        verbose_name = "Endereço do Membro"
        verbose_name_plural = "Endereços dos Membros"

    def __str__(self):
        return f'{self.get_member_name} - {self.address_line}'

    @property
    def get_member_name(self):
        return self.member.complete_name if hasattr(self, 'member') else ''


class MemberPhone(Phone):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Telefone do Membro"
        verbose_name_plural = "Telefones dos Membros"

    def __str__(self):
        return f'{self.get_name} - {self.number_formatted}'

    @property
    def get_name(self):
        return self.member.complete_name if hasattr(self, 'member') else ''


class MemberFiliationType(models.Model):
    code = models.CharField(max_length=3, verbose_name='Código do Tipo de Membro')
    name = models.CharField(max_length=30, verbose_name='Nome do Tipo de Membro')
    description = models.TextField(verbose_name="Descrição", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tipo do Membro"
        verbose_name_plural = "Tipos dos Membros"

    def __str__(self):
        return f'{self.code} - {self.name}'


class MemberFiliation(models.Model):
    joined_at = models.DateField(verbose_name='Data de Ingresso')
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    member_filiation_type = models.ForeignKey(MemberFiliationType, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Filiação do Membro"
        verbose_name_plural = "Filiações dos Membros"

        constraints = [
            models.UniqueConstraint(fields=['member', 'organization'], name='unique_member_in_organization'),
        ]

    def __str__(self):
        return f'{self.get_member_name} - {self.get_organization_name}'

    @property
    def get_member_name(self):
        return self.member.complete_name if hasattr(self, 'member') else ''

    @property
    def get_organization_name(self):
        return self.organization.our_blessed_lady_title.name if hasattr(self, 'organization') else ''


class PostOffice(models.Model):
    code = models.CharField(max_length=3, verbose_name='Código do Tipo de Membro')
    name = models.CharField(max_length=30, verbose_name='Nome do Tipo de Membro')
    description = models.TextField(verbose_name="Descrição", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Cargo de Oficial"
        verbose_name_plural = "Cargos de Oficiais"

    def __str__(self):
        return f'{self.code} - {self.name}'


class PostOfficeMemberFiliation(models.Model):
    joined_at = models.DateField(verbose_name='Data de Ingresso')
    member_filiation = models.ForeignKey(MemberFiliation, on_delete=models.CASCADE)
    post_office = models.ForeignKey(PostOffice, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Cargo de Oficial do Membro na Organização"
        verbose_name_plural = "Cargos de Oficiais dos Membros na Organizações"

        constraints = [
            models.UniqueConstraint(fields=['member_filiation', 'post_office'],
                                    name='unique_postoffice_to_memberfiliation'),
        ]

    def __str__(self):
        return f'{self.post_office.code} | {self.post_office.name} - {self.member_filiation.member.complete_name}'



