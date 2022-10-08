# Generated by Django 4.1.1 on 2022-10-08 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0011_alter_organizationphone_options'),
        ('members', '0004_memberphone'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberFiliation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_at', models.DateField(verbose_name='Data de Ingresso')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.member')),
            ],
        ),
        migrations.CreateModel(
            name='MemberFiliationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3, verbose_name='Código do Tipo de Membro')),
                ('name', models.CharField(max_length=30, verbose_name='Nome do Tipo de Membro')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostOffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3, verbose_name='Código do Tipo de Membro')),
                ('name', models.CharField(max_length=30, verbose_name='Nome do Tipo de Membro')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostOfficeMemberFiliation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_at', models.DateField(verbose_name='Data de Ingresso')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('member_filiation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.memberfiliation')),
                ('post_office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.postoffice')),
            ],
        ),
        migrations.AddField(
            model_name='memberfiliation',
            name='member_filiation_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.memberfiliationtype'),
        ),
        migrations.AddField(
            model_name='memberfiliation',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.organization'),
        ),
    ]
