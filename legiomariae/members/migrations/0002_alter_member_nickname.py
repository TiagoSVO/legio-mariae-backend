# Generated by Django 4.1.1 on 2022-10-06 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='nickname',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Apelido'),
        ),
    ]