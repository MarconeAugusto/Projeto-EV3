#!/usr/bin/env python3
# coding: utf-8
from self import self
from InterfaceGrafica import *

a = 2

pos1 = [3,0]
pos2 = [0,4]
pos3 = [4,5]
lista2 = [pos1, pos2, pos3]


@Pyro4.expose
@Pyro4.oneway
class PrincipalSS:
    def modoJogo(self):
        global a
        if a == 2:  # modo Manual
            # Create new threads
            thread1 = Configuracao(1)
            # Start new Threads
            thread1.start()
        if a == 1:  # modo autonomo
            print("Implementar modo Autonomo")
            # Create new threads
            thread2 = Configuracao(2)  # inicia servidor Pyro4 do SS
            thread3 = Configuracao(3)  # inicia interface Autonomo , alterar depois
            thread4 = Configuracao(4)  # Registra o servidor de nomes
            # Start new Threads
            thread2.start()
            time.sleep(1)
            thread3.start()
            thread4.start()
            time.sleep(1)
            ClienteSR.MovimentoAutonomo(self)

    def getListaCacas(self):
        global lista2
        return lista2

    def removeCaca(self):
        global lista2
        return lista2


if __name__ == '__main__':
    PrincipalSS.modoJogo(self)
