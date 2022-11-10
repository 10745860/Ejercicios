#!/usr/bin/env python3
"""
Autor : Andreea Cristina Mihai <10745860@iespenyagolosa.es>
Fecha   : 09/11/22
Propósito:  Calcular mínimo, máximo y media.
"""

numeros=int(input('Cuántos valores vas a introducir?: '))
minimo=100000000000000000000000000
maximo=0
suma=0
media=0
for i in range(1,numeros+1):
    num=int(input(f'Dime el número {i}: '))
    suma += num
    if numeros<minimo:
        minimo=numeros
    elif numeros>maximo:
        maximo=numeros   
media=suma/numeros    
print(f'El número más pequeño de los introducidos es: ')
print(f'El número más grande de los introducidos es: ')   
print(f'La media de los números introducidos es: ')


  



