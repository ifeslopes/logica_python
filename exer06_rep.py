import random
lista=[0]
x=int()
y=int()

for i in range(1,13):
	lista.append(random.randint(1,100))
	print(lista[i],end=" ")
print()
	
x=int(input('Entre com valor de X '))
y=int(input('Entre com valor de Y '))
print('O valor da soma de {} com {} = {} '.format(lista[x],lista[y],lista[x]+lista[y]))