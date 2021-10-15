"""
Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis 
compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.
"""

valores = [3, 4, 7, 8, 1, 6, 9]
#valores = list(range(4,11))

# Valores na ordem
valores.sort()
print(valores)

#Em ordem contrária 
valores.sort(reverse=True)
print(valores)

print(f"\nTamanho da Lista: {len(valores)}")