"""
Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor
retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""
import ex109


print('\033[1;36m-=-\033[m'*15)
valor = float(input('Digite o preço: R$ '))
print('\033[1;36m-=-\033[m'*15)


print('\033[1;31m-=-\033[m'*20)
print(f'A metade de {ex109.moeda(valor)} é {ex109.metade(valor)}')
print(f'O dobro de {ex109.moeda(valor)} é {ex109.dobro(valor)}')
print('\033[1;31m-=-\033[m'*20)

print('\033[1;31m-=-\033[m'*20)
print(f'Aumentando 10%, temos {ex109.aumentar(valor,10,True)}')
print(f'Subtraindo 10%, temos {ex109.diminuir(valor,10,True)}')
print('\033[1;31m-=-\033[m'*20)
