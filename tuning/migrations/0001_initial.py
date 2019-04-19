# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-10 03:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ultima_alteracao', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ultima_alteracao', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('cnpj', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='ParcelaComissao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ultima_alteracao', models.DateTimeField(auto_now=True)),
                ('valor', models.DecimalField(decimal_places=5, max_digits=18)),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tuning.Colaborador')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ultima_alteracao', models.DateTimeField(auto_now=True)),
                ('total', models.DecimalField(decimal_places=5, max_digits=18)),
                ('status', models.CharField(choices=[(b'0', b'Cancelado'), (b'1', b'Em or\xc3\xa7amento'), (b'2', b'Conclu\xc3\xaddo')], max_length=2)),
                ('numero', models.IntegerField()),
                ('informacoes_adicionais', models.TextField()),
                ('data_emissao', models.DateTimeField()),
                ('criador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tuning.Colaborador')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tuning.Empresa')),
            ],
        ),
        migrations.AddField(
            model_name='parcelacomissao',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tuning.Pedido'),
        ),
        migrations.AddIndex(
            model_name='empresa',
            index=models.Index(fields=[b'nome'], name='tuning_empr_nome_a5e087_idx'),
        ),
        migrations.AddIndex(
            model_name='empresa',
            index=models.Index(fields=[b'slug'], name='tuning_empr_slug_f9538d_idx'),
        ),
        migrations.AddIndex(
            model_name='empresa',
            index=models.Index(fields=[b'email'], name='tuning_empr_email_503360_idx'),
        ),
        migrations.AddField(
            model_name='colaborador',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tuning.Empresa'),
        ),
        migrations.AddIndex(
            model_name='pedido',
            index=models.Index(fields=[b'data_emissao', b'numero'], name='tuning_pedi_data_em_434cc1_idx'),
        ),
        migrations.AddIndex(
            model_name='colaborador',
            index=models.Index(fields=[b'email'], name='tuning_cola_email_cae4da_idx'),
        ),
    ]
