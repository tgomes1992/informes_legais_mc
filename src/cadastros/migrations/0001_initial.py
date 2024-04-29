# Generated by Django 5.0.4 on 2024-04-24 18:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cd_jcot', models.CharField(default='', max_length=25)),
                ('cd_o2', models.CharField(default='', max_length=200)),
                ('cd_amplis', models.CharField(default='', max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fundo',
            fields=[
                ('cnpj', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('tipo', models.CharField(choices=[('A', 'Aberto'), ('F', 'Fechado')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Cota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('valor', models.FloatField()),
                ('ativo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.ativo')),
            ],
        ),
        migrations.AddField(
            model_name='ativo',
            name='fundo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.fundo'),
        ),
    ]