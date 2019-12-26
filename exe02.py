x=int(input("Entre com nunero X"))
y=int(input("Entre com nunero Y"))
z=int(input("Entre com nunero Z"))
tipo=str(input("entre com tipo de media G,P,H,A:  "))
if (x<=0) or (y<=0) or(z<=0):
	print("não foi possivel calcular media numero igual ou baixo de 0")
else:
	if (tipo=="G") or (tipo=="g"):
		me=((x*y*z)**(1/3))
		print("%.2f"%(me))
	elif (tipo=="P") or (tipo=="p"):
		me=(x+2*y+3*z)/6
		print("%.2f"%(me))
	elif (tipo=="H") or (tipo=="h"):
		me=1/(1/x+1/y+1/z)
		print("%.2f"%(me))
	elif (tipo=="A") or (tipo=="a"):
		me=(x+y+z)/3
		print("%.2f"%(me))