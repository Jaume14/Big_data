#PART 1: Preparació
import pandas as pd #importem la llibreria

#Obrim el document
#Per la seva mida necessitem utilitzar chunks
#Utilitzarem només les columnes que necessitem: data i viewers
df = pd.read_csv("feb_23_es_simple.csv", chunksize=1000000, sep="\t", usecols=["captured_at", "game_name", "viewer_count"])
print("document obert")

#Creem les llistes necessaries per utilitzar posteriorment
llista_dataframes = []
#Per controlar el procés havia utilitzat un contador
count = 0
print(f"El contador està a {count}")


#PART 2: Processament
#Per a cada chunk iterem
for chunk in df:
	#Agrupem els elements amb el mateix nom del joc i contem quants hi ha
	df2 = chunk.groupby(['captured_at', 'game_name'])['viewer_count'].sum()
	#Codi de control count
	print(count)
	count +=1
	#afegim cada df a la llista
	llista_dataframes.append(df2)

print('Tots els df estan a la llista')

#PART 3: Exportació
#Concatenem els df de la llista per crear un df amb tots
final_frame_1 = pd.concat(llista_dataframes)
print('Un únic df creat')
print(final_frame_1)
'''
#Com que hi haurà jocs dividits en chunks, tornarem a agrupar-los i sumarem els valors de recompte
final_frame_1.groupby(['captured_at', 'game_name'])['viewer_count'].sum()
print(f'Provisionalment el df es: \n {final_frame_1}')
'''
#Exportem el document a csv per després poder representar visualment les dades
final_frame_1.to_csv("ex_3.csv")
print("Tenim exportat el document csv anomenat ex_3.csv")