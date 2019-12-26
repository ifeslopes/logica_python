import random
idade=[0]
cont=0
total=float()
media=float()
for i in range(1,31):
	idade.append(random.randint(1,40))
	total+=idade[i]
	print(idade[i],end= " ")
print()
print("A MÉDIA DE IADE: %.1f"%(total/i))
media=(total/i)
for j in  (idade):
	if (j>13) and (media<j):
	 cont+=1
print("A quantidade de aluno acima dos 13 anos e acima da media é:",cont)