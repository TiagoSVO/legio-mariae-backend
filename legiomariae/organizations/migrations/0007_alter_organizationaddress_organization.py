# Generated by Django 4.1.1 on 2022-10-02 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0006_organizationaddress_linked_church'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationaddress',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='organizations.organization', verbose_name='Organização'),
        ),
    ]