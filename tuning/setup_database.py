import os
from threading import Thread
from time import sleep

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tuning4newcomers.settings")

import django

django.setup()

from mixer.backend.django import mixer

from tuning.models import Empresa, Colaborador, Pedido, ParcelaComissao, DadosEmpresa


# t1 = Thread(target=lambda: mixer.cycle(30000).blend(Empresa))
# # t2 = Thread(target=lambda: mixer.cycle(0).blend(Colaborador, empresa=mixer.SELECT))
# t3 = Thread(target=lambda: mixer.cycle(10000).blend(Pedido, empresa=mixer.SELECT, criador=mixer.SELECT))
# t4 = Thread(target=lambda: mixer.cycle(1000).blend(ParcelaComissao, empresa=Empresa.objects.get(id=100), pedido=(pedido for pedido in Pedido.objects.filter(empresa_id=100)),
#                                                     colaborador=mixer.SELECT))


def loading():
    while True:
        print 'Loading...'
        # print(Empresa, Empresa.objects.all().count())
        # print(Pedido, Pedido.objects.all().count())
        # print(ParcelaComissao, ParcelaComissao.objects.all().count())
        # print(Colaborador, Colaborador.objects.all().count())
        print(DadosEmpresa, DadosEmpresa.objects.all().count())
        sleep(2)


t5 = Thread(target=loading)
t5.start()
#
# t1.start()
# # t2.start()
# # t3.start()
# t4.start()


mixer.cycle(12000).blend(DadosEmpresa, empresa=mixer.SELECT)