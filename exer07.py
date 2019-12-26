var=str(input("entre com texto"))
esp=str(' ')
vaga=["a","e","i","o","u","A","E","I","O","U"]
contv=int()
conts=int()
for aqui in var:
	if aqui==esp:
		conts+=1
	elif aqui in vaga:
		contv+=1
print("Quantidade vogais",conts)
print("Quantidade de espaço",contv)	