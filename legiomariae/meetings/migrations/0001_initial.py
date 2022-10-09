# Generated by Django 4.1.1 on 2022-10-09 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Data da Reunião')),
                ('start_at', models.TimeField(verbose_name='Início da Reunião')),
                ('place_address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Local da Reunião')),
                ('initial_prayer', models.BooleanField(default=True, verbose_name='Orações Iniciais')),
                ('rosary_prayer', models.BooleanField(default=True, verbose_name='Oração do Terço')),
                ('spiritual_read', models.CharField(blank=True, max_length=255, null=True, verbose_name='Leitura Espiritual')),
                ('standing_instructions_readed', models.BooleanField(default=False, verbose_name='Instrução Permanente')),
                ('catena_prayer', models.BooleanField(default=True, verbose_name='Oração da Catena')),
                ('allocutio', models.TextField(blank=True, null=True, verbose_name='Allocutio')),
                ('announcements', models.TextField(blank=True, null=True, verbose_name='Avisos e Outros Assuntos')),
                ('final_observations', models.TextField(blank=True, null=True, verbose_name='Observações Finais')),
                ('final_prayer', models.BooleanField(default=True, verbose_name='Oração da Catena')),
                ('end_at', models.TimeField(verbose_name='Final da Reunião')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Reunião',
                'verbose_name_plural': 'Reuniões',
            },
        ),
    ]
