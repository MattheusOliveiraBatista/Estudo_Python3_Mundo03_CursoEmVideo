'''
Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python. 
As tuplas são variáveis compostas e imutáveis que permitem armazenar vários 
valores em uma mesma estrutura, acessíveis por chaves individuais.
'''

#Tuplas são IMUTÁVEIS!!!

# Tupla  = (), Lista = [], Dicionário = {}

#lanche = 'Hambúrguer', 'Suco', 'Pizza','Pudim' OU

lanche = ('Hambúrguer', 'Suco', 'Pizza','Pudim', 'Batata Frita')
print(sorted(lanche)) #Ordenação dos valores
print(lanche)
print(lanche[-2]) #Pizza
print(lanche[:2])#Hambúrguer e Suco
print(lanche[-4:]) #Outra forma de imprir na ordem


#Índice 0 = -4;     1 = -3;     2 = -2 ;    3 = -1
print('\n')
print(10*'=')

for cont in range(0,len(lanche)):
    print(f'[{cont}] = {lanche[cont]}')    
print(10*'=')
print('\n')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')


'''
for c in   lanche:
    print(f'Eu vou comer {cont} agora')
print(10*'=')

print('Comi pra Caramba!! =)')

'''

print(f'\nTamanho da Tupla: {len(lanche)}')

#print('Tuplas São IMUTÁVEIS')
# ERRO, NÃO PODEMOS MUDAR O VALOR DA TUPLA
# lanche[0] = 'Strogonoff'
#print(lanche[0])