# coding=utf-8
from django.db import models

STATUS_PEDIDO = (
    ('0', 'Cancelado'),
    ('1', 'Em orçamento'),
    ('2', 'Concluído'),
)


class Empresa(models.Model):
    ultima_alteracao = models.DateTimeField(auto_now=True)

    nome = models.CharField(max_length=200)
    slug = models.SlugField(max_length=20)
    email = models.EmailField(max_length=50)
    cnpj = models.CharField(max_length=14)

    class Meta:
        indexes = [
            models.Index(fields=['nome'], name='idx_nome'),
            models.Index(fields=['email'], name='idx_email'),
        ]


class Colaborador(models.Model):
    empresa = models.ForeignKey(Empresa)
    ultima_alteracao = models.DateTimeField(auto_now=True)

    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=75)

    class Meta:
        indexes = [
            models.Index(fields=['email'], name='idx_email'),
        ]


class Pedido(models.Model):
    empresa = models.ForeignKey(Empresa)
    ultima_alteracao = models.DateTimeField(auto_now=True)

    total = models.DecimalField(max_digits=18, decimal_places=5)
    status = models.CharField(max_length=2, choices=STATUS_PEDIDO)
    numero = models.IntegerField()
    informacoes_adicionais = models.TextField()
    data_emissao = models.DateTimeField()

    criador = models.ForeignKey(Colaborador)

    class Meta:
        indexes = [
            models.Index(fields=['data_emissao', 'numero'], name='idx_data_emissao_numero'),
        ]


class ParcelaComissao(models.Model):
    ultima_alteracao = models.DateTimeField(auto_now=True)

    valor = models.DecimalField(max_digits=18, decimal_places=5)

    pedido = models.ForeignKey(Pedido)
    colaborador = models.ForeignKey(Colaborador)


class DadosEmpresa(models.Model):
    ultima_alteracao = models.DateTimeField(auto_now=True)

    numero_fiscal = models.DecimalField(max_digits=18, decimal_places=5)

    empresa = models.ForeignKey(Empresa)
