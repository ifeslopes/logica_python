ab10=int()
ac10=int()
ac20=int()
lucro=int()
for i in range(1,4):
 compra=int(input("Valor da compra"))
 venda=int(input("Valor da venda"))
 lucro=((venda-compra)/compra)*100
 print("%.0f%%"%(lucro))
 if lucro>20:
 	print("%.0f%%"%(lucro))
 	ac20+=1
 elif 10<lucro<20:
 	print("%.0f%%"%(lucro))
 	ac10+=1
 elif lucro<10:
 	print("%.0f%%"%(lucro))
 	ab10+=1
print("Produtos Abaixo de 10%",ab10)
print("Produtos Acima de 10%",ac10)
print("Produtos Acima de 20%",ac20)
 	
 	


