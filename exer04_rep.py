import time
lista=[2,6,8,88,99,7,5,33,66,90]
m=0
d=int(1)
T=int()
c=0
print(lista)

m=int(input("entre com posicao do vetor: "))
for i in (lista):
  if m ==i:
  	T=i
  	c=d
  	#break
  d+=1
if m==T:
	print("posição: %d Valor no vetor: %d"%(c,T))
else:
	print('VALOR %d NAO ENCONTRADO!'%m)
  
