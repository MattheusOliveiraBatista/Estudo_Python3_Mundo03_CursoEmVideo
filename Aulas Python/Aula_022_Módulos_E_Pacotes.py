"""
Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo
como criar módulos em Python e reutilizar nossos códigos em outros projetos.
Vamos aprender também como agrupar vários módulos em um pacote, ampliando
ainda mais a modularização em grandes projetos em Python.
"""
import Módulos_Da_Aula022

num = int(input('Digite um número inteiro: '))
fat = Módulos_Da_Aula022.fatorial(num)

print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {Módulos_Da_Aula022.dobro(num)}.')
print(f'O triplo de {num} é {Módulos_Da_Aula022.triplo(num)}.')
