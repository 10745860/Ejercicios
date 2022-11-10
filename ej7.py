#!/usr/bin/env python3
"""
Autor : Andreea Cristina Mihai <10745860@iespenyagolosa.es>
Fecha   : 07/11/22
Propósito: Escribir una lista de números
"""

n=int(input('Dime un número: '))
if n>0:
    for i in range(0,n+1):
        print(i,end=", ")
else:
    for i in range (0,n-1, -1):
        print(i, end=", ")

print()                
    

