from csv import reader
from PerWordAnalisys import *

#6.4  Cuáles son los usuarios que más reviews negativos y positivos dan en promedio.

usuariosPositivos={}
usuariosNegativos={}
usuariosTotales={}

# open file in read mode
with open('./files/CleanData.csv', encoding="utf8") as read_obj:
	# pass the file object to reader() to get the reader object
	csv_reader = reader(read_obj)

	contador=0

	# Iterate over each row in the csv using reader object
	for row in csv_reader:

		if(contador==0):
			contador+=1
			continue
		
		sentimiento=perWordAnalisys(row[-1])
		if(sentimiento>0):
			#Positivo
			try:
				usuariosPositivos[row[3]]+=1
				usuariosTotales[row[3]]+=1
			except Exception as e:
				usuariosPositivos[row[3]]=1
				usuariosTotales[row[3]]=1
			
			
		elif(sentimiento<0):
			try:
				usuariosNegativos[row[3]]+=1
				usuariosTotales[row[3]]+=1
			except Exception as e:
				usuariosNegativos[row[3]]=1
				usuariosTotales[row[3]]=1
		
			
		contador+=1

		if(contador==500):
			break




for usuario in usuariosTotales:
	try:
		usuariosPositivos[usuario]/=usuariosTotales[usuario]		
	except Exception as e:
		pass

	try:
		usuariosNegativos[usuario]/=usuariosTotales[usuario]		
	except Exception as e:
		pass

print()
dictSortedPositivos=sorted(usuariosPositivos.items(), key=lambda x: x[1],reverse=True)
print("Top 5 usuarios que más reviews positivos dan en promedio:")
control=0
for i in dictSortedPositivos:
	control+=1
	print(i)
	if(control==5):
		break
print()
dictSortedNegativos=sorted(usuariosNegativos.items(), key=lambda x: x[1],reverse=True)
print("Top 5 usuarios que más reviews negativos dan en promedio:")
control=0
for i in dictSortedNegativos:
	control+=1
	print(i)
	if(control==5):
		break
#['brand', 'manufacturer', 'name', 'reviews.username', 'reviews.didPurchase', 'reviews.doRecommend', 'reviews.rating', 'reviews.text']