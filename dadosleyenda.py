#! /usr/bin/env python
# -*- coding: utf-8 -*-

from random import *
from heapq import *
es_cero = 0

print "¿Dados tirados?"
numero = input()
print "¿Dados guardados"
guardados = input()
lista_dados = []
lista_criticos = []
contador_diez = 0
print "¿Repetir dieces? si/no"
opcion = raw_input()
lista_guardados = []

def comprobador(lista):
    global lista_criticos, lista_dados, es_cero, contador_diez, lista_guardados, guardados
    while len(lista_dados) < numero:
        lista_dados.append(randrange(0, 10, 1))

    lista_sin_criticos = []
    if opcion == "si":
        for i in lista:
            if i != 0:
                lista_sin_criticos.append(i)

            if i == 0:
                while es_cero == 0:
                    contador_diez += 1
                    es_cero = randrange(0, 10, 1)
                lista_sin_criticos.append(es_cero)
    elif opcion == "no":
        lista_sin_criticos = list(lista_dados)

    lista_guardados = nlargest(guardados, lista_sin_criticos)
    return lista_sin_criticos


print comprobador(lista_dados), " con ", contador_diez, " dieces", " es decir: ", sum(lista_guardados) + 10 * contador_diez
