Com a enunciat i font d'informació he utilitzat l'enllaç següent:
	https://adriapadilla.github.io/bigdata-uab/ejercicios/ejercicio_3.html

### Neteja del fitxer
Primer de tot necessitem conèixer mínimament el fitxer. Veurem quines columnes tenim per netejar el fitxer csv. En aquest cas utilitzem el següent codi per obtenir les columnes.
```Python
import pandas as pd  
 
# Per estalviar temps de càrrega utilitzarem nrows i usecols.  
df = pd.read_csv("feb_23_es_simple.csv",  
                 sep='\t',  #utilitzarem \t (tabulador) perquè ho indica a l'enunciat 
                 nrows=10000,  #perquè no ens peti el procés)  
  
for col in df.columns:
    print(col) #imprimim els noms de les columnes  
```
Obtenim el resultat:
	- captured_at
	- streamer_name
	- streamer_id
	- position
	- viewer_count
	- game_name
	- game_id

En les proves he utilitzat nrows per simplificar els processos i fer que apareguin més ràpidament els errors.
D'altra banda, per saber en quin moment del procés estava l'execució també he inclòs alguns print perquè aparegui al terminal l'estat.
Generalment, també he dividit els exercicis en tres parts:
1. Importar llibreries, netejar les dades en un DataFrame dividit en chunks i crear les variables principals.
2. Fer els càlculs, iterant per a cada chunk.
3. Agrupar els chunks, fer el calcul final (perquè hi ha dades dividides en més d'un chunk) i exportar les dades en csv.

## 1. Quina ha estat l'evolució d'espectadors (captura a captura) durant el període?

```Python
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
   Imprimia i augmentava en 1 el contador per controlar el procés mentre provava el codi   print(count)   count +=1   '''   #afegim cada df a la llista  
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
```

Després de desenvolupar el codi, hem obtingut els següents gràfics amb Tableau. A partir d'aquests s'han pogut extreure la informació i les conclusions que exposo a continuació.

![Imatge](https://github.com/Jaume14/Big_data/blob/main/Treball_Twitch/Pasted%20image%2020230416171223.png)
![[Pasted image 20230416171223.png]]
La captura comença l'1 de febrer i acaba el 28 de febrer. En aquest gràfic minut a minut podem veure que hi ha pics i valls cíclics. Tot i així, hi ha pics que pugen molt més amunt que d'altres. El primer pic que destaca el trobem entre els dies 5 i 7 de febrer. També hi ha algun altre dia en que el pic ha sobresortit però no és més d'un dia seguit, excepte a final de mes. Els dies 26, 27 i 28 hi ha els màxims d'audiències, arribant a més d'un milió i mig d'espectadors.

![[Pasted image 20230416171758.png]]
En quant, al comportament cíclic esmentat abans, correspon a les hores dels dies. A la nit, entre les 19h i les 4h es concentren la majoria d'espectadors, mentre que al matí i migdia nl'audiència és molt baixa.



## 2. Quines són les categories més vistes i en què s'han realitzat més hores de directe?
Per dur a terme aquesta tasca he separat l'exercici en dues parts: primer extreure les categories més vistes i després saber en quins jocs s'han realitzat més hores en directe.

Codi de jocs més vistos.
```Python
#PART 1  
import pandas as pd #importem la llibreria  
  
#Obrim el document  
#Per la seva mida necessitem utilitzar chunks  
#Utilitzarem només les columnes que necessitem: data i viewers  
df = pd.read_csv("feb_23_es_simple.csv", nrows = 10000, chunksize=10000, sep="\t", usecols=["captured_at","game_name","viewer_count"])  
print("document obert")  
  
#Creem les llistes necessaries per utilitzar posteriorment  
llista_dataframes = []  
#Per controlar el procés havia utilitzat un contador  
count = 0  
  
#PART 2  
#Per a cada chunk iterem  
for chunk in df:  
   #Agrupem els elements amb la mateixa data i sumem els seus viewers  
   df2 = chunk.groupby("game_name")["viewer_count"].sum().reset_index()  
   #Imprimia i augmentava en 1 el contador per controlar el procés mentre provava el codi  
   print(count)  
   count +=1  
   #afegim cada df a la llista  
   llista_dataframes.append(df2)  
  
print('Tots els df estan a la llista')  
  
#PART 3  
#Concatenem els df de la llista per crear un df amb tots  
final_frame_1 = pd.concat (llista_dataframes)  
print('df únic creat')  
  
#Com que hi haurà dates dividides en chunks, tornarem a fer l'agrupació i suma per dates  
final_frame_2 = final_frame_1.groupby("game_name")["viewer_count"].sum()  
  
print(final_frame_2)  
  
#ordenem el df  
final_frame_2 = final_frame_2.sort_values(by=["viewer_count"])  
  
#Exportem el document a csv per després poder representar visualment les dades  
final_frame_2.to_csv("ex_2.1.csv")  
print("Tenim exportat el document csv anomenat ex_2.1.csv")
```

Codi de jocs amb més hores de directe.
```Python
#PART 1: Preparació  
import pandas as pd #importem la llibreria  
  
#Obrim el document  
#Per la seva mida necessitem utilitzar chunks  
#Utilitzarem només les columnes que necessitem: data i viewers  
df = pd.read_csv("feb_23_es_simple.csv", chunksize=1000000, sep="\t", usecols=["captured_at","game_name"])  
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
   df2 = chunk.groupby("game_name").count()  
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
  
#Com que hi haurà jocs dividits en chunks, tornarem agrupar-los i sumarem els valors de recompte  
final_frame_1.groupby("game_name")["captured_at"].sum()  
print(f'Provisionalment el df es: \n {final_frame_1}')  
  
#Com que cada aparició suposa 15min (1/4 hora) dividim per obtenir el nombre d'hores  
final_frame_1['captured_at'] = final_frame_1["captured_at"].div(4)  
print(final_frame_1)  
  
#Exportem el document a csv per després poder representar visualment les dades  
final_frame_1.to_csv("ex_2_2.csv")  
print("Tenim exportat el document csv anomenat ex_2_2.csv")
```

![[Pasted image 20230416173720.png]]

![[Pasted image 20230416194134.png]]

Comparant aquestes dues mètriques podem veure que la majoria dels jocs amb més espectadors també són els que tenen més hores de joc. Cal destacar un parell de casos molt concrets que es troben en els 10 jocs amb més espectadors, i en canvi no apareixen en els que tenen més hores jugades. Són els "Sports" i "Special Events". Aquesta diferència evidencia que molt poques hores de directes en aquesta categoria suposen una acumulació molt alta (probablement simultània) d'espectadors.



## 3. Com han evolucionat (captura a captura) aquestes categories al llarg del mes?

```Python
#PART 1: Preparació  
import pandas as pd #importem la llibreria  
  
#Obrim el document  
#Per la seva mida necessitem utilitzar chunks  
#Utilitzarem només les columnes que necessitem: data i viewers  
df = pd.read_csv("feb_23_es_simple.csv", chunksize=1000000, sep="\t", usecols=["captured_at","game_name", "viewer_count"])  
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
   df2 = chunk.groupby(['captured_at', 'game_name'], as_index=False)['viewer_count'].sum()  
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
  
#Com que hi haurà jocs dividits en chunks, tornarem a agrupar-los i sumarem els valors de recompte  
final_frame_1.groupby(['captured_at', 'game_name'], as_index=False)['viewer_count'].sum()  
print(f'Provisionalment el df es: \n {final_frame_1}')  
  
#Exportem el document a csv per després poder representar visualment les dades  
final_frame_1.to_csv("ex_3.csv")  
print("Tenim exportat el document csv anomenat ex_3.csv")
```

![[Pasted image 20230416174715.png]]

L'evolució de la majoria de categories és força estable, especialment "Just Chatting". Trobem quatre pics de la categoria "Sports" als dies 5, 12 i 19. El dia 26, a final de més també apareix un creixement molt important a "Sports" que dobla qualsevol altre pic. El mateix que passa al dia 28 amb "Minecraft" i "Just Chatting". El 28 de febrer també hi ha un creixement molt gran de "Special Events".
Un últim fenòmen que cal destacar és "Hogwarts Legacy", que apareix al dia 7 i va decaient fins a perdre's amb la resta de categories.



## 4. Quina és la distribució dels streamers si els classifiquem per volums d'audiència i hores fetes?

```Python
#PART 1: Preparació  
import pandas as pd #importem la llibreria  
  
#Obrim el document  
#Per la seva mida necessitem utilitzar chunks  
#Utilitzarem només les columnes que necessitem: data, streamer i viewers  
df = pd.read_csv("feb_23_es_simple.csv", chunksize=100000, sep="\t", usecols=["captured_at", "streamer_name", "viewer_count"])  
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
   df2 = chunk.groupby(['streamer_name'])['viewer_count'].sum().reset_index()  
   df2 ['recompte'] = chunk.groupby(['streamer_name'])['captured_at'].count().reset_index()['captured_at']  
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
  
#Com que hi haurà jocs dividits en chunks, tornarem a agrupar-los i sumarem els valors de recompte  
final_frame_2 = final_frame_1.groupby('streamer_name')["viewer_count"].sum().reset_index()  
final_frame_2['recompte'] = final_frame_1.groupby(['streamer_name'])['recompte'].sum().reset_index()['recompte'].div(4)  
  
print(f'Provisionalment el df es: \n {final_frame_2}')  
  
#Exportem el document a csv per després poder representar visualment les dades  
final_frame_2.to_csv("ex_4.csv")  
print("Tenim exportat el document csv anomenat ex_4.csv")
```

![[Pasted image 20230416200621.png]]
Amb aquest gràfic podem veure que hi ha una majoria que té molt pocs espectadors, tant si fant moltes hores de directe com si en fan molt poques. Trobem algun streamer que no deixa de fer directe en ningún moment i que sí que alguns viewers, com viviendoenlacalle o IJEnz. Després trobem tota una agruàció que tenen molts espectadors que no fan més de 150hores i que agrupen entre 10 milions i 48 milions d'audiència. Son: kingleague, ibai, IlloJuan, ElSpreen, juansguarnizo i ElMariana.



## 5. Quina ha estat l'evolució (captura a captura) de la desviació estàndard al volum d'espectadors? En quins moments les audiències estan més polaritzades i en quins moments la distribució és més uniforme?

```Python
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
```

![[Pasted image 20230416202154.png]]
![[Pasted image 20230416202740.png]]

L'evolució de la desviació del volum d'espectadors coincideix amb el comportament cíclic de l'evolució de màxims d'espectadors. S'observa un comportament cíclic que coincideix amb les hores del dia. A la tarda i nit es polaritzen els espectadors, mentre que a partir de les 22h i fins la 1h, l'audiència es va fent uniforme. Els pics de desviació també coincideixen amb els moments de més audiència del mes. En canvi en les hores vall els espectadors estan distribuïts de manera més uniforme, ja que la desviació és molt menor. Podem concloure que aquells que moments en que hi ha més espectadors també són aquells en els que l'audiència està més polaritzada.
