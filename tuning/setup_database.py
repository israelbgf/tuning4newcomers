import itertools
import os

import random
from pycpfcnpj import gen
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tuning4newcomers.settings")
django.setup()

from mixer.backend.django import mixer

from tuning.models import Empresa, Vendedor, Pedido, Item

for i in range(100):
    empresa = mixer.blend(Empresa, cnpj=gen.cnpj())
    print('')
    print('Criando Empresa {}'.format(empresa.id))

    vendedores = mixer.cycle(random.randint(1, 30)).blend(Vendedor, empresa=empresa)

    vendedores_pool = itertools.cycle(vendedores)
    for j in range(200):
        pedido = mixer.blend(Pedido, empresa=empresa, vendedor=next(vendedores_pool))
        print('Criando Pedido {}'.format(pedido.id))
        items = mixer.cycle(random.randint(1, 50)).blend(Item, pedido=pedido)
