# Generated by Django 4.1.1 on 2022-10-07 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0010_alter_organizationaddress_organization'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organizationphone',
            options={'verbose_name': 'Telefone da Organização', 'verbose_name_plural': 'Telefoness ddas Organizações'},
        ),
    ]
