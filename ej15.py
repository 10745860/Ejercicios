#!/usr/bin/env python3
"""
Autor : Andreea Cristina Mihai <10745860@iespenyagolosa.es>
Fecha   : 25/10/22
Propósito: Convertidor de suma.
"""

print('Suma de las cifras de un número')
numero=input('Escribe un número: ')
lista=list(numero)
cifra1=int(lista[0])
cifra2=int(lista[1])
cifra3=int(lista[2])
cifra4=int(lista[3])
suma=cifra1+cifra2+cifra3+cifra4

print(f'La suma de las cifras del número {numero} es {suma}.')