qsexm=int()
qsexf=int()
m_idad=int()
maior=int()
nome_m=str()

for i in range(1,21):
	nome=str(input("Entre com none: "))
	sexo=str(input("Entre M masculi e F femino: "))
	idade=int(input("Entre com idade: "))
	if sexo=="M" or sexo=="m":
		m_idad+=idade
		qsexm+=1
	elif sexo=="F" or sexo=="f":
		qsexf+=1
	if maior<idade:
		maior=idade
		nome_m=nome
print("Q/ de Homens: %d Q/ de Mulheres: %d" %(qsexm,qsexf))
print("Media de iade masculina: %f "%(m_idad/qsexm))
print("pessoa com mais idade: ",nome_m)