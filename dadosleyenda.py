#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Este script es para dados de leyenda,
# con el sistema dados tirados y guardados
from random import randrange
from heapq import nlargest
# importamos lo que hace falta
# el nlargest es para elegir
# los valores más altos de la lista
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
# inicializamos variables y escribimos el menú


def comprobador(lista):
    global lista_criticos, lista_dados, es_cero, contador_diez,\
        lista_guardados, guardados
    while len(lista_dados) < numero:
        lista_dados.append(randrange(0, 10, 1))
# tirar dados hasta que se alcanza el número
# de dados a tirar
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
# Según se elija repetir dieces o no
    lista_guardados = nlargest(guardados, lista_sin_criticos)
# Se guardan los más altos normalmente
    return lista_sin_criticos


print comprobador(lista_dados), " con ", contador_diez, " dieces",\
    " es decir: ", sum(lista_guardados) + 10 * contador_diez
# En el resultado se muestra la lista completa de dados, por si
# se quisieran elegir valores inferiores o bien revisar la tirada
