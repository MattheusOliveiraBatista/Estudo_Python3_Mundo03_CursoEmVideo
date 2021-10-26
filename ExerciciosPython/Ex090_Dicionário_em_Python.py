"""
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""
pessoa = dict()
situacao = ''
pessoa['nome'] = str(input('Nome: '))
pessoa['média'] = float(input('Média de {} : '.format(pessoa['nome'])))

if 7 <= pessoa['média'] <= 10:
    situacao = '\033[1;32mAprovado\033[m'

elif 5 <= pessoa['média'] < 7:
    situacao = '\033[1;33mRecuperação\033[m'

elif pessoa['média'] < 5:
    situacao = '\033[1;31mReprovado\033[m'
else:
    print('Média Inválida!')

print('\n')

print(20 * '\033[1;31m-=-\033[m')
print(f'  - nome é igual a {pessoa["nome"]}')
print(f'  - média é igual a {pessoa["média"]}')
print(f'  - situação é igual a {situacao}')
print(20 * '\033[1;31m-=-\033[m')
