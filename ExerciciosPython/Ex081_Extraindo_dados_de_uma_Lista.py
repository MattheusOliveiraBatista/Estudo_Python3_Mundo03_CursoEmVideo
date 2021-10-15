"""
 Crie um programa que vai ler vários números e colocar em uma lista.                  
 Depois disso, mostre:                                    
 A) Quantos números foram digitados.          
 B) A lista de valores, ordenada de forma decrescente.
 C) Se o valor 5 foi digitado e está ou não na lista.
 """
lista = []
 
while True:
    lista.append(int(input('Digite um valor: ')))    
    op = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    
    if op in 'Nn':
        break

print('\n')
print(30*'-')
print(f'Lista: {lista}')
print(f"Tamanho da Lista: {len(lista)}")
listaD = lista.sort(reverse=True)
print(f"Lista decrescente: {listaD}")

if 5 not in lista:
    print('O valor 5 não faz parte da lista :(')
else:
    print('O valor 5 está na lista!! :)')


print(30*'-')

