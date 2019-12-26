cont=int()
n=int(input("entre com valor N: "))
m=int(input( "entre com valor M: "))
for i in range(1,m+1):
	if i%n==0:
		cont+=1
		print(i)
print(cont)