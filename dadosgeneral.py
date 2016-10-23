#! /usr/bin/env python
# -*- coding: utf-8 -*-
# está preparado para python 2.7
from random import randrange


es_cero = 0
numero = 4
lista_dados = []
lista_criticos = []
contador_diez = 0
dificultades = []
pifias = 0

# lista de variables que usaremos, autoexplicativas


def comprobador(lista):
    global lista_criticos, lista_dados, es_cero, contador_diez,\
        dificultades, pifias
    while len(lista_dados) < numero:
        lista_dados.append(randrange(0, 10, 1))
# número no es más que el número de dados que
# queremos tirar, mientras no alcancemos ese número,
# se siguen tirando dados
    lista_sin_criticos = []
    if opcion == "si":
        for i in lista:
            if i != 0:
                lista_sin_criticos.append(i)
# en el caso de que queramos diezes repetidos
# a continuación se suman al contador de los
# críticos
            if i == 0:
                while es_cero == 0:
                    contador_diez += 1
                    es_cero = randrange(0, 10, 1)
                lista_sin_criticos.append(es_cero)
    elif opcion == "no":
        lista_sin_criticos = list(lista_dados)
# lo siguiente es teniendo en cuenta la dificultad
# seleccionada, los dados que la superan cuentan
# como éxito, se añaden a la lista
    for i in lista_sin_criticos:
        if i >= difi:
            dificultades.append(i)
    for i in lista_sin_criticos:
        if i == 1:
            pifias += 1

    return lista_sin_criticos
# Y este es el menú y la salida
print "¿Dificultad?"
difi = input()
print "¿Dados?"
numero = input()
print "¿Repetir dieces?, si/no"
opcion = raw_input()
print comprobador(lista_dados), "y", contador_diez, "dieces, en total:",\
       len(dificultades) + contador_diez - pifias, "éxitos"
