import random
lista=[]
cont=int(0)
maior=0
ind=0
f=int(10)
for i in range(0,50):
 lista.append(random.randint(1,100))
 cont+=1
 if maior<lista[i]:
 	maior=lista[i]
 	ind=cont
for i in(lista):
	if maior==i:
		print('\033[31m%d\033[m'%i,end=' ')
	else:
		print(i,end=" ")
print()
print("O maior numero é {} A posição é {}".format(maior,ind))
