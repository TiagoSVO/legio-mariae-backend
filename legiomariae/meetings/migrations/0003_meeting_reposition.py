# Generated by Django 4.1.1 on 2022-10-09 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0002_meeting_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='reposition',
            field=models.BooleanField(default=False, verbose_name='Reposição'),
        ),
    ]
