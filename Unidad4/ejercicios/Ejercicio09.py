#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 18 feb. 2020

@author: Robert G
'''


def es_bisiesto(anio):
    if anio % 4 == 0:
        anyo = "Es bisiesto"
        return anyo
    elif anio % 4 != 0:
        anyo = "No es bisiesto"
        return anyo

   
while True:  # Este while le uso para seguir jugando
    numero = int(input("Introduce un año y te dire si es bisiesto o no: "))
    while numero < 1920 or numero > 2120:  # Con este while condiciono un rango de anyos
        print("Te has pasado o no has llegado!!")
        numero = int(input("Introduce un año y te dire si es bisiesto o no: "))
    print es_bisiesto(numero)
    resp = int(input("Pulsa 1 para seguir o 0 para salir: "))
    if resp == 0:
        print("Has salido del programa, espero que vuelvas pronto :)")
        break  # año Salgo del primer while
