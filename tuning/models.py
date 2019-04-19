# coding=utf-8
from django.db import models

STATUS_PEDIDO = (
    ('0', 'Cancelado'),
    ('1', 'Orçamento'),
    ('2', 'Concluído'),
)


class Empresa(models.Model):
    ultima_alteracao = models.DateTimeField(auto_now=True)
    cnpj = models.CharField(max_length=14)


class Vendedor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=75)

    empresa = models.ForeignKey(Empresa)


class Pedido(models.Model):
    total = models.DecimalField(max_digits=18, decimal_places=5)
    status = models.CharField(max_length=2, choices=STATUS_PEDIDO)
    numero = models.IntegerField()
    informacoes_adicionais = models.TextField()
    data_emissao = models.DateTimeField()

    empresa = models.ForeignKey(Empresa)
    vendedor = models.ForeignKey(Vendedor)


class Item(models.Model):
    valor = models.DecimalField(max_digits=18, decimal_places=5)
    percentual_desconto = models.DecimalField(max_digits=2, decimal_places=2)

    pedido = models.ForeignKey(Pedido)
