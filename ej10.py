#!/usr/bin/env python3
"""
Autor : Andreea Cristina Mihai <10745860@iespenyagolosa.es>
Fecha   : 08/11/22
Propósito: Escribir un número y calcular su factorial
"""
numero=int(input('Dime un número: '))
factorial=1

for i in range(1,numero+1):
    factorial=factorial*i

print(f'El factorial de {numero} es {factorial}')
    

  



