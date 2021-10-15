"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar',  'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'\nNa palavra \033[1;32m{p.upper()}\033[m temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end= ' ')

