"""
Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python. Os dicionários são
variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.
"""

# dados = {} #
# Ou
#dados = dict()

dados = dict()

dados = {
    'nome':'Pedro',
    'idade': 21
}

dados['sexo'] = 'M'
print(dados)

# Deletando Idade
# del dados['idade']
# print(dados)

# Valores dos campos
print(dados.values())
# Nome dos campos
print(dados.keys())
# Valores e nomes dos campos
print(dados.keys())