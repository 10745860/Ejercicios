#!/usr/bin/env python3
"""
Autor : Andreea Cristina Mihai <10745860@iespenyagolosa.es>
Fecha   : 08/11/22
Propósito: Escribir una lista de números
"""

num=int(input('Dime un número positivo: '))

while num<=0: 
    print('¡Te he pedido un numero positivo!')
    num=int(input('Dime un número positivo: '))
for i in range(0,num+1):
    print(i,end=", ")

print()
for i in range(num,-1,-1):
    print(i, end=", ")

print()
for i in range(1,num):
    print(i,end=", ")

print()
for i in range(num,0,-1):
    print(i,end=", ")

print()
for i in range(0,num+1):
    print(i,end=", ")    

for i in range(num-1,-1,-1):
    print(i,end=", ")
print()
    

