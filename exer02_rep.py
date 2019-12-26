lista1=[23,55,77,66,86,1]
lista2=[0,1,2,3,4,5,6,7,8,9,10]
lista3=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
c=0
f=0
while c<15:
	c+=1
	if c<=5:
		
		lista3[c]=lista1[c]
		print(lista3[c])
	else:
		f+=1
		lista3[c]=lista2[f]
		print(lista3[c])
		
print(lista3)
	