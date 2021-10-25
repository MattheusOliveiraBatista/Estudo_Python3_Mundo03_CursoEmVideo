"""
Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python. Os dicionários são
variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.
"""
locadora = []


filme_Um = {
    'Titulo': 'Star Wars',
    'Ano': 1977,
    'Diretor': 'George Lucas'

}

filme_Dois= {
    'Titulo': 'Avengers',
    'Ano': 2012,
    'Diretor': 'Joss Whedons'

}

filme_Tres = {
    'Titulo': 'Matrix',
    'Ano': 1999,
    'Diretor': 'Wachpwski'

}

#for k,v in filme_Um.items():
    #print(f'O {k} é {v}')


locadora.append(filme_Um)
locadora.append(filme_Dois)
locadora.append(filme_Tres)

for i in locadora:
    print(f'O filme {i["Titulo"]} foi lançado em {i["Ano"]} pelo Diretor {i["Diretor"]}')