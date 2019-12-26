ve=int(input('entre com valor de vetor'))
ve1=ve
ve2=int()
for i in range(ve+1):
	print("Valor de vetor",i)
	ve2=ve1-i
	if (ve2%2==0):
		print("valor par da ordem invert",ve2)