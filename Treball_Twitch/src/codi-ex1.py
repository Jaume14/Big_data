#PART 1
import pandas as pd #importem la llibreria

#Obrim el document
#Per la seva mida necessitem utilitzar chunks
#Utilitzarem només les columnes que necessitem: data i viewers
df = pd.read_csv("feb_23_es_simple.csv", chunksize=10000, sep="\t", usecols=["captured_at","viewer_count"])
#print("document obert")

#Creem les llistes necessaries per utilitzar posteriorment
llista_dataframes = []
#Per controlar el procés havia utilitzat un contador
#count = 0

#PART 2
#Per a cada chunk iterem
for chunk in df:
	#Agrupem els elements amb la mateixa data i sumem els seus viewers
	df2 = chunk.groupby("captured_at")["viewer_count"].sum().reset_index()
	'''
	Imprimia i augmentava en 1 el contador per controlar el procés mentre provava el codi
	print(count)
	count +=1
	'''
	#afegim cada df a la llista
	llista_dataframes.append(df2)

#print('Tots els df estan a la llista')

#PART 3
#Concatenem els df de la llista per crear un df amb tots
final_frame_1 = pd.concat (llista_dataframes)
#print('df únic creat')

#Com que hi haurà dates dividides en chunks, tornarem a fer l'agrupació i suma per dates
final_frame_2 = final_frame_1.groupby("captured_at")["viewer_count"].sum()

#Exportem el document a csv per després poder representar visualment les dades
final_frame_2.to_csv("ex_1.csv")
#print("Tenim exportat el document csv anomenat ex_1.csv")
