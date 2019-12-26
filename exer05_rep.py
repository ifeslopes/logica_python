import random
lista=[]
lista2=[]
m=0
n=0
t=float()
c=0
r=0
for i in range(0,20):
	m+=1
	lista.append(random.randrange(1,21))
	lista2.append(i)
while m>10:
	m-=1
	n+=1
	
	lista2[m]=lista[m]
	lista[m]=lista[n]
	lista[n]=lista2[m]
	#n+=1
	print("\033[35m%d:\033[m"%lista[n],end="<-->")
	print("\033[34m%d:\033[m"%lista[m])

lista.pop(0)
for i in (lista):
	print("\033[34m{}\033[m".format(i)if r>9else '\033[35m{}\033[m'.format(i),end=" ")
	r+=1
	
