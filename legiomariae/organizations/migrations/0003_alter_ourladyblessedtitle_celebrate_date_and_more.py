# Generated by Django 4.1.1 on 2022-10-01 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_ourladyblessedtitle_alter_organizationtype_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourladyblessedtitle',
            name='celebrate_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Comemoração'),
        ),
        migrations.AlterField(
            model_name='ourladyblessedtitle',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição'),
        ),
    ]