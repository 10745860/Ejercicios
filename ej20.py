#!/usr/bin/env python3
"""
Autor : Andreea Cristina Mihai <10745860@iespenyagolosa.es>
Fecha   : 03/11/22
Propósito: Adivinar un número entre un intervalo de dos
"""

from random import randrange
num1=int(input('Valor mínimo: '))
num2=int(input('Valor máximo: '))
aleatorio=randrange(num1,num2)
intentos=1
print(f'A ver si adivinas un número entre {num1} y {num2}.') 
numero=int(input('Escribe un número: '))
while numero !=aleatorio:
    intentos +=1
    if numero<aleatorio:
        numero=int(input('¡Demasiado pequeño! Inténtalo de nuevo: '))
    else:
        numero=int(input('¡Demasiado grande! Inténtalo de nuevo: '))

print('¡Acertaste! Te ha costado {intentos} intemtos.')
