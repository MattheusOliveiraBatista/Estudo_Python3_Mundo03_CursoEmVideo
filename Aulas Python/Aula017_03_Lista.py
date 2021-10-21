"""Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis compostas
que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais. """

teste = []
galera = []

teste.append('Matheus')
teste.append(21)
galera.append(teste[:])
# galera.append(teste)

teste[0] = "Gustavo"
teste[1] = 40

# galera.append(teste)
galera.append(teste[:]) #Assim simboliza a cópia das informações

print(f'Lista Teste: {teste}')
#print(f'Lista Galera: {galera}')



