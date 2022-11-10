#!/usr/bin/env python3
"""
Autor : Andreea Cristina Mihai <10745860@iespenyagolosa.es>
Fecha   : 08/11/22
Propósito: Escribir una lista de números pares
"""
numero_inicial=int(input('Dime el valor inicial: '))
numero_final=int(input('Dime el valor final: '))

for i in range(numero_inicial,numero_final,):
    if i%2==0:
        print(i,end=", ")
print()

  



