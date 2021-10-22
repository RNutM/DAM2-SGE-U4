#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 17 feb. 2020

@author: Robert G
'''

num = input("Introduce un numero: ")

if num == 0:
    print("Este numero es cero")
elif num % 2 == 0:
    print("Este numero es par")
else:
    print("Este numero es impar")
