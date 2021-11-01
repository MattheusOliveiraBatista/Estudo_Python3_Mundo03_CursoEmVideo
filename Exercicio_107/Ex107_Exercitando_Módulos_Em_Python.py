"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), 
dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

"""
import ex107

print('\033[1;36m-=-\033[m'*10)
valor = float(input('Digite o preço: R$ '))
print('\033[1;36m-=-\033[m'*10)

print()

print('\033[1;31m-=-\033[m'*10)
ex107.Metade(valor)
ex107.Dobro(valor)
ex107.MaisDezPorCento(valor)
ex107.MenosDezPorCento(valor)
print('\033[1;31m-=-\033[m'*10)
