lista=[0]
c=0
while c<100:
	if c%2==0:
		lista.append(1)
		#print(c)
		#print(lista[c])
	else:
		lista.append(0)
		#print(c)
		#print(lista[c])
	c+=1
print(lista)