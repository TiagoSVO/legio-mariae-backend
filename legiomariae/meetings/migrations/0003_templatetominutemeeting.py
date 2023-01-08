# Generated by Django 4.1.1 on 2022-12-05 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0011_alter_organizationphone_options'),
        ('meetings', '0002_meeting_orientations'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateToMinuteMeeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome do Template')),
                ('description', models.TextField()),
                ('template_format', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organizations.organization')),
            ],
            options={
                'verbose_name': 'Modelo para Ata',
                'verbose_name_plural': 'Modelos Para Atas',
            },
        ),
    ]