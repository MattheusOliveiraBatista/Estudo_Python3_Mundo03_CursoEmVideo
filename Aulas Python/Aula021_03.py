"""
Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive Help em Python,
o uso de docstrings para documentar nossas funções, argumentos opcionais para dar mais dinamismo em funções Python,
escopo de variáveis e retorno de resultados.
"""
#help(print())

def somar( a = 0, b = 0, c = 0):
    """
    -> Faz a soma dos três valores e mostra o resultado na tela.
    :param a: primeiro valor.
    :param b: segundo valor.
    :param c: terceiro valor.
    Função criado por Matheus Batista
    """
    s = a + b + c
    #print(f'A soma vale {s}')
    return s


#somar(1, 3, 6)
resp1 = somar(3,2,5)
resp2 = somar(2,2)
resp3 = somar(6)

print(f'Os resultados foam {resp1}, {resp2} e {resp3}')