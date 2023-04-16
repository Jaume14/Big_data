#PART 1
import pandas as pd #importem la llibreria

#Obrim el document
#Per la seva mida necessitem utilitzar chunks
#Utilitzarem només les columnes que necessitem: data i viewers
df = pd.read_csv("feb_23_es_simple.csv",nrows=1000000, chunksize=100000, sep="\t", usecols=["captured_at","viewer_count"])
print("document obert")

#Creem les llistes necessaries per utilitzar posteriorment
llista_dataframes = []
#Per controlar el procés havia utilitzat un contador
count = 0

#PART 2
#Per a cada chunk iterem
for chunk in df:
	#Agrupem els elements amb la mateixa data i sumem els seus viewers
	df2 = chunk.groupby("captured_at", group_keys=True)[ "viewer_count"].apply(lambda x: x)
	#Imprimia i augmentava en 1 el contador per controlar el procés mentre provava el codi
	print(count)
	count +=1
	#per imprimir el primer chunk d'exemple
	if (count==1):
		print(df2)
	#afegim cada df a la llista
	llista_dataframes.append(df2)

print('Tots els df estan a la llista')

#PART 3
#Concatenem els df de la llista per crear un df amb tots
final_frame_1 = pd.concat (llista_dataframes)
print('df únic creat')

#Com que hi haurà dates dividides en chunks, tornarem a fer l'agrupació i càlcul per dates
final_frame_2 = final_frame_1.groupby("captured_at", group_keys=True).std().round(2)
print("Desviació afegida")

print(final_frame_2)

'''
#Exportem el document a csv per després poder representar visualment les dades
final_frame_2.to_csv("ex_5.csv")
print("Tenim exportat el document csv anomenat ex_5.csv")'''