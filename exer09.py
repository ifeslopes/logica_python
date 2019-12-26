n=int(input("Entre com valor de N: "))
m=int(input("Entre com valor de M: "))
soma=int()
for i in range(n,m):
	if i%5==0 or i%11==0:
		soma+=i
		print(i)
print(soma)