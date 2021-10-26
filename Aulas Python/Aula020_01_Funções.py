"""
Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python.
Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python.
Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.
"""


def lin():
    print(30 * '\033[1;31m-\033[m')


lin()
print('     CURSO EM VÍDEO     ')
lin()
lin()
print('     APRENDA PYTHON     ')
lin()
lin()
print('   GUSTAVO GUANABARA    ')
lin()


def mensagem(msg):
    print(30 * '\033[1;31m-\033[m')
    print(msg)
    print(30 * '\033[1;31m-\033[m')


mensagem('      SISTEMAS DE ALUNOS')
