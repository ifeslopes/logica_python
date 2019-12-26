import random
nota=[]
matri=[]
total=0
media=0
c=0
while c<4:
	matri.append(int(input('entre com matricula: ')))
	nota.append(float(input("Entre com as notas: ")))
	total+=nota[c]
	c+=1

media=total/c
print('Media: {:.2f}'.format(media))
for i in range(c):
	if nota[i]>media:
		print('Notas acima da Medida')
		print('matricula{} nota: {:.2f}'.format(matri[i],nota[i]))
	elif nota[i]<media:
		print('Notas abaixo da Medida')
		print('matricula{} nota:\033[31m {:.2f}\033[m'.format(matri[i],nota[i]))