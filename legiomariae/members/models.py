from django.db import models


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


class MemberAddress()