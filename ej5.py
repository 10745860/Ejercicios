#!/usr/bin/env python3
"""
Autor : Andreea Cristina Mihai <10745860@iespenyagolosa.es>
Fecha   : 25/10/22
Propósito: Cálculo de áreas.
"""

print('Cálculo de áreas - Elige una figura geométrica: ')
print('a) Triángulo')
print('b) Circulo')
figura=input('Qué figura quieres calcular (escribe T o C)? ').upper()
if figura=='T' :
    base=float(input('Escribe la base: '))
    altura=float(input('Escribe la altura: '))
    area1=base*altura/2
    print(f'Un triángulo de base {base} y altura {altura} tiene un área de {area1}.')
elif figura=='C' :
    radio=float(input('Escribe el radio: '))
    area2=3.14*radio**2
    print(f'Un círculo de radio {radio} tiene un área de {area2}')
else:
    print('No es un círculo o un triángulo')