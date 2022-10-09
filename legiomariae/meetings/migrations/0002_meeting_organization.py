# Generated by Django 4.1.1 on 2022-10-09 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0011_alter_organizationphone_options'),
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='organizations.organization', verbose_name='Organização'),
            preserve_default=False,
        ),
    ]
