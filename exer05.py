num=int(1)
den=int(2)
soma=float()
soma=num/den
print(num)
print('---')
print(den)
print()

for i in range(2,21):
	
	num+=2 
	den*=2
	if i%2==0:
		soma-=num/den
		print(num)
		print('---')
		print(den)
		print()
	else:
		soma+=num/den
		print(num)
		print("---")
		print(den)
		print()
print(soma)