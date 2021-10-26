"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""
pessoa = {}
galera = []
media = soma = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F]')).upper().strip()[0]

    if pessoa['sexo'] not in 'MF':
        print('ERRO! Responda apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper().strip()[0]

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']

    galera.append(pessoa.copy())

    decisao = str(input('Deseja Continuar? [S/N]')).upper().strip()[0]
    if decisao in "N":
        break
    elif decisao == 'S':
        continue
    else:
        print('ERRO! Responda apenas S ou N.')
        decisao = str(input('Deseja Continuar? [S/N]')).upper().strip()[0]

print('\n')
print(20 * '\033[1;31m-=-\033[m')
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'B) A média de idade é de {soma / len(galera):5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}  ', end='')

print()
print(f'D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('  ',end='')
        for k,v in p.items():
            print(f'{k} = {v}; ', end='')
print('\n')
print('  <<  ENCERRANDO  >>>  ')
print(20 * '\033[1;31m-=-\033[m')
