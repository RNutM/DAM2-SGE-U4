#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 17 feb. 2020

@author: Robert G
'''

lista = []  # Declaramos una lista vacia

# Aqui ponemos cuantas veces queremos que pida un numero
for x in range(3):
    numero = input("Introduce un numero entero:")
    lista.append(numero)
# ordenamos la lista
lista.sort()
# imprimimos la lista    
print("Los numeros ordenados son: ") , (lista)
