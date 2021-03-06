# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-19 14:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ultima_alteracao', models.DateTimeField(auto_now=True)),
                ('cnpj', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=5, max_digits=18)),
                ('percentual_desconto', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=5, max_digits=18)),
                ('status', models.CharField(choices=[(b'0', b'Cancelado'), (b'1', b'Or\xc3\xa7amento'), (b'2', b'Conclu\xc3\xaddo')], max_length=2)),
                ('numero', models.IntegerField()),
                ('informacoes_adicionais', models.TextField()),
                ('data_emissao', models.DateTimeField()),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tuning.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=75)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tuning.Empresa')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tuning.Vendedor'),
        ),
        migrations.AddField(
            model_name='item',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tuning.Pedido'),
        ),
    ]
