"""
Exercício Python 105: Faça um programa que tenha uma função notas() que pode
receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
"""


def notas(*n, sit=False):
    """
    -> Função para analisar e situações de vários alunos.
    :param n: um ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não mostrar a nota.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = {'total': len(n), 'maior': max(n), 'menor': min(n), 'média': sum(n) / len(n)}

    if sit:
        if r['média'] >= 7:
            r['situação'] = '\033[1;32mBOA\033[m'
        elif r['média'] >= 5:
            r['situação'] = '\033[1;33mRAZOÁVEL\033[m'
        else:
            r['situação'] = '\033[1;31mRUIM\033[m'

    return r

resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
# help(notas)
