a = (2, 4, 5, 7)
b = (5, 8, 1, 2)
print(a)
print(b)
 
c = a + b # 2, 4, 5, 7, 5, 8, 1, 2
print(len(c)) #Tamanho da tupla  
print(c)
print(sorted(c)) #Ordenação
print(c.count(5)) #Qtds de vezes o n° 5
print(c.index(5))

pessoas = ('Matheus', '21', 'M', '75.6') #Aceita diversos tipos
del(pessoas) #Apaga a tupla
print(pessoas)