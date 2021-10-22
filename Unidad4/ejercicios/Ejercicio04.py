#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 17 feb. 2020

@author: Robert G
'''
par = [2, 4, 6, 8]
impar = [1, 3, 5, 7]
resultado = 0

# 4.1 - SUMAR (+) El primer elemento de la lista par + el ultimo elemento de la lista impar
resultado = par[0] + impar[-1]
print "El resultado de la operacion 4.1 es: ", resultado

# 4.2 - RESTAR (-) El segundo elemento de la lista par - el segundo elemento de la lista impar.
resultado = par[1] - impar[1]
print "El resultado de la operacion 4.2 es: ", resultado

# 4.3 - MULTIPLICAR (*) El ultimo elemento de la lista par * el tercer elemento de la lista impar.
resultado = par[-1] * impar[2]
print "El resultado de la operacion 4.3 es: ", resultado

# 4.4 - DIVIDIR (/) El ultimo elemento de la lista par / el primer elemento de la lista par.
resultado = par[-1] / par[0]
print "El resultado de la operacion 4.4 es: ", resultado

# 4.5 - SUMAR (+) El segundo elemento de la lista impar + el tercer elemento de la lista par + el ultimo elemento de la lista impar.
resultado = impar[1] + par[2] + impar[-1]
print "El resultado de la operacion 4.5 es: ", resultado
