"""
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e  idade em um arquivo de texto simples.

O sistema só vai ter duas opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

Exercício Python 115a: Vamos criar um menu em Python, usando modularização.
Exercício Python 115b: Vamos ver como fazer acesso a arquivos usando o Python.
Exercício Python 115c: Vamos finalizar o projeto de acesso a arquivos em Python.
"""

#from Exercicio115.Library.Interface import *
from Library.Interface import *
from Library.Arquivo import *
from time import sleep
import os

arq = 'CursoEmVideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])

    if resposta == 1:
        #Opção de listar um conteúdo do arquivo
        lerArquivo(arq)
        sleep(4)
        os.system("cls")
    elif resposta == 2:
        #Cadastrar nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('\033[1;36mNome: \033[m'))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
        sleep(2)
        os.system("cls")
    elif resposta == 3:
        cabeçalho('Saindo do sistema...Até logo!')
        sleep(4)
        os.system("cls")
        break
    else:
        print('\033[1;31mERROR! Digite uma opção válida!\033[m')
        sleep(2)
        os.system("cls")

    sleep(2)
