# Generated by Django 4.1.1 on 2022-10-01 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0004_remove_state_phone_code'),
        ('organizations', '0004_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='organization_parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organizations.organization', verbose_name='Vinculado à:'),
        ),
        migrations.CreateModel(
            name='OrganizationAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line', models.CharField(max_length=250, verbose_name='Endereço')),
                ('address_number', models.CharField(blank='True', max_length=10, null='True', verbose_name='Número')),
                ('complement', models.CharField(blank='True', max_length=100, null='True', verbose_name='Complemento')),
                ('zipcode', models.CharField(max_length=8, verbose_name='CEP')),
                ('latitude', models.CharField(blank=True, max_length=9, null=True)),
                ('longitude', models.CharField(blank=True, max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='addresses.city', verbose_name='Cidade')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='addresses.country', verbose_name='País')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.organization', verbose_name='Organização')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='addresses.state', verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Endereço da Organização',
                'verbose_name_plural': 'Endereços das Organização',
            },
        ),
    ]