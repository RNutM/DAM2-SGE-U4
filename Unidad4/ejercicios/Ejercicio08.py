#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 18 feb. 2020

@author: Robert G
'''

lista = []

# Aqui ponemos cuantas veces queremos que pida un numero
for x in range(3):
    numero = input("Introduce un numero entero para añadir a la lista:")
    lista.append(numero)


def max_in_list(lista):
    return max(lista)


print max_in_list(lista)
