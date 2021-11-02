"""
Nessa aula, vamos ver como o Python permite tratar erros e criar respostas
a essas exceções. Aprenda como usar a estrutura try except no Python de uma forma simples.
"""
# x não foi inicializado, isso é uma exceção.
# print(x)


# n = int(input('Digite um número: '))
# print(f'Você digitou o número {n}')

# Não teve erro, teve uma exceção devido o tipo do input.
# ValueError: invalid literal for int() with base 10: 'Dez'.

# --------------------------------------
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
# except:
#   print('Deu erro! :(')

# except Exception as erro:
#   print(f'Problema encontrado foi {erro.__class__}.')
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except KeyboardInterrupt:
    print('O usuário preferiu finalizar o programa.')

except Exception as erro:
    print(f'O erro encontrado foi{erro.__cause__}')
else:
    print(f'A divisão é igual a {r:.1f}.')
finally:
    print('Volte sempre!')
# ----------------------
# Excção ao tentar dividir por zero.
# ZeroDivisionError: division by zero.


lst = [0, 1, 2]
# print(lst[3])
# Exceção, tentar exibir o índice 3, ele não existe.


"""
try: #TENTE
 operação

except # Exceção
falhou

else: # Senão
 deu certo
 
finally: 
  certo/falha
"""
