# Generated by Django 4.1.1 on 2022-10-20 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0006_alter_meeting_final_prayer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minutemeeting',
            name='description',
            field=models.TextField(default='### NÃO PREENCHIDA ###', verbose_name='Descrição completa da Ata'),
        ),
    ]