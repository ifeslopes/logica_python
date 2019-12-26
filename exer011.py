n=int(input("Informe o valor de N: "))
s=float()
for i in range(1,n+1):
	if i%2!=0:
		s+=(2*i-1)/(n-(i-1))
	else:
		s+= -(2*i-1)/(n-(i-1))
print("%.1f"%s)