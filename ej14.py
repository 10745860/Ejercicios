#!/usr/bin/env python3
"""
Autor : Andreea Cristina Mihai <10745860@iespenyagolosa.es>
Fecha   : 10/11/22
Propósito:  Escribir una frase que cambie las vocales por una misma igual
"""
frase='tengo una hormiquita en la barriga'
vocal=input('Dime una vocal: ')
VOCALES='aeiou'
frase_nueva=[]
for i in range(len(frase)):
    if frase[i] in VOCALES:
        frase_nueva.append(vocal)
    else:
        frase_nueva.append(frase[i])    
    
print=(f'La frase es ahora: {frase_nueva} ')


  



