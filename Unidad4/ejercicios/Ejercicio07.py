#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 18 feb. 2020

@author: Robert G
'''
meses = {1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio",
         7:"Julio", 8:"Agosto", 9:"Septiembre", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"}

while True:  # Este while le uso para seguir jugando 
    numero = int(input("Introduce un numero entero del 1 al 12: "))
    while numero < 1 or numero > 12:  # Con este while condiciono un rango de numeros
        print("Te has pasado o no has llegado!!")
        numero = int(input("Introduce un numero entero del 1 al 12: "))
    print meses[numero]
    resp = int(input("Pulsa 1 para seguir o 0 para salir: "))
    if resp == 0:
        print("Has salido del programa, espero que vuelvas pronto :)")
        break  # Salgo del primer while
