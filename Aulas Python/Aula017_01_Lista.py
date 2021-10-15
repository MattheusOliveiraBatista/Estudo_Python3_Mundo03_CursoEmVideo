"""
Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis 
compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.
"""
# Listas estão entre colchetes
# Lista são mutáveis

lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim']

print(lanche)

# Atualizando o elemento
lanche[3] = 'Picolé'

# Adicionando elemnento
lanche.append('Cooke')

# Adicionando cachorro - quente, na posição 0
# Todos os elementos serão deslocados para a direita
# Inserindo cachorro quente na posição 0
lanche.insert(0,'Cachorro quente')

# Apagando o ultimo elemento
del lanche[3]

# Apagando o ultimo elemento ou o índice que desejarmos
#lanche.pop() - O último elemento
# lanche.pop(1)

# Apagando através do valor
lanche.remove('Pizza')
print(lanche)
