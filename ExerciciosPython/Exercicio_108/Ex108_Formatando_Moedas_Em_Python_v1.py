"""
Adapte o código do desafio #107, criando uma função adicional chamada moeda()
que consiga mostrar os números como um valor monetário formatado.
"""
import ex108


print('\033[1;36m-=-\033[m'*15)
valor = float(input('Digite o preço: R$ '))
taxa = int(input('Digite um valor para a taxa (0 a 100): '))
print('\033[1;36m-=-\033[m'*15)

if taxa == 0:
    taxa = 10


print()

print('\033[1;31m-=-\033[m'*20)
print(f'A metade de {ex108.moeda(valor)} é {ex108.moeda(ex108.metade(valor))}')
print(f'O dobro de {ex108.moeda(valor)} é {ex108.moeda(ex108.dobro(valor))}')
print('\033[1;31m-=-\033[m'*20)
print(f'Você digitou {taxa}%. Serão aplicados {taxa}% a mais e a menos.')
print('\033[1;31m-=-\033[m'*20)
print(f'Aumentando {taxa}%, temos {ex108.moeda(ex108.maisdezporcento(valor,taxa))}')
print(f'Subtraindo {taxa}%, temos {ex108.moeda(ex108.menosdezporcento(valor,taxa))}')
print('\033[1;31m-=-\033[m'*20)
