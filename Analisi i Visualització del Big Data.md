#apunts #BigData
# 14/02/2023: Pycharm, Obsidian i Python

### Link web, exercicis i resum de classe
https://adriapadilla.github.io/bigdata-uab/

## PyCharm
Perquè pycharm? Perquè utilitza un entorn virtual perquè no hi hagi problemes amb la versió del Python (que a cada ordinador de classe pot haver-hi instalada una versió diferent).
Comandos bàsics:
--> Ctrl + L neteja pantalla
--> Ctrl + C aturar procés

## Obsidian
Coses bàsiques del programa:
#etiqueta #prova
# Títol 1 (# )
## Títol 2 (## )
### Títol 3 (### )
I així els que calguin.
Text normal.
```
Això és un text de codi i s'ha d'obrir amb (```)
```

## Remember de Python
### Cadena de text
Hi ha problemes amb les cometes, no confondre-les.
--> Utilitzar simples/dobles
Els dos exemples són cadenes de text.
``` "cadena de text" 'cadena de text' ```

### Print
--> Mostrar a pantalla el que sigui
--> Cal separar amb comes els diferents tipus de coses:
```"L'usuari", usuari, "té", likes, "likes."```

### Números
--> Integers: sense punt: 1
--> Float: amb punt: 1.2
--> Per passar de string a integer: int(numero_string)
```Python
for n in notas:  
    nota_numerica = int(nota)
```

### Variables
--> Text directament escrit amb un igual al final: nom_variable = 1
--> Les variables es poden sobreescriure, la que mana és la última per ordre de lectura del text.

### Funcions
#### str
--> Uneix diferents tipus de dades en un string:
```frasestring = str"L'usuari "+usuari +"té" +likes +"likes."```

### Comentaris
--> Per fer comentaris utilitzar el hashtag (#)
--> Les tres cometes creen un paragraf de comentari
```
"""Això és un comentari""" 
# Això també és un comentari
``` 

### Llistes
Són elements que poden recollir un conjunt de dades de qualsevol tipus.
``` llista_noms = [Marc, Pau, Adrià] ```
També es poden fer llistes de llistes.
```llista_tots_alumnes = [llista_noms, Maria, Pere, Paula]```
Per afegir elements a les llistes .append o .extend
```Python
llista_noms = llista_noms.append(nou_nom)
```

# 21/02/2023: Bucles, funcions amb llistes i límits
## Bucles For/If
Volem analitzar tota una llista i classificar-la.
```Python
llista_noms = ["carme", "joan"]  #Aquesta llista ja la tenim
  
for nom in llista_noms:  #recorrem per a cada element de la llista i classifiquem
    if nom == "joan":  
        print(nom)  
    else:  
        print(nom + " no és en Joan")
```

Per fer més eficient el bucle, es pot utilitzar: f{nom}
```Python
llista_noms = ["carme", "joan"]  #Aquesta llista ja la tenim
  
for nom in llista_noms:   #recorrem per a cada element de la llista i classifiquem
    if nom == "joan":  
        print(nom)  
    else:  
        print(f"{nom} no és en Joan")
```

Si hi ha més condicions intermitges utilitzem: elif
```Python
numeros = [1,2,3,6,7,8,10,15]  #Aquesta llista ja la tenim
  
for n in numeros:  #recorrem per a cada element de la llista i classifiquem
    if n<6:  
        print(f"{n} és menor que 6") #si és menor de 6 fem això
    elif n==6:  
        print(f"{n} és igual que 6") #si no és l'anterior i és 6 fem això.
    else:  
        print(f"{n} és major que 6") #si no és cap de les anteriors, és major que 6
```

## Funcions natives de Python
Un exemple és print.

### Len
Per veure com de llarga és la llista utilitzem: len
```Python
numeros = [1,2,3,6,7,8,10,15] #Aquesta llista ja la tenim
print(len(numeros)) #imprimeix la llargada
```

### Zip()
Per aparellar dues llistes entre elles utilitzem: zip().
--> Veure exercici B

### Exercicis de classe
#### Exercici A
```Python
txt = "esto es un ejercicio"  
print(txt)  
  
  
nota = 10  
asignatura = "BigData"  
  
txt1 = f"En la asignatura {asignatura} he obtenido un {nota}"  #combinem el print amb f" i posem els valors entre claudàtors {}
print(txt1)  
  
nota = 5  
txt1 = f"En la asignatura {asignatura} he obtenido un {nota}"  
print(txt1)
```

#### Exercici B
```Python
#Un compañero te ha mandado dos listados: las notas y los nombres de los alumnos a quienes corresponden dichas notas:  
notas = ["5","7","6","4","8","2"]  
alumnos = ["jaume","carla","pere","adrià","rafael","agnès"]  
  
for nota, nom in zip(notas, alumnos):  #combinem les llistes per ordre
    nota_numerica = int(nota)  
#Debes sumar 1 punto a cada una de las notas.  
    nota_final = nota_numerica + 1  
#Imprime el resultado junto al nombre del correspondiente alumno de tal manera que: "var_alumno ha obtenido un var_nota".  
    print(f"{nom} ha obtenido un {nota_final}")
```

### .index
Per veure la posició d'un element en una llista
```Python
llista = ["adria", "carla", "joan", "pere"]  
nom = "joan"  
if nom in llista:  
    print("si")  
    position = llista.index(nom)  
    print(position)  #imprimim la posició que hem extret
else:  
    print("no") #si no està a la llista diem que no
```

### set()
Per esborrar valors repetits set()
```Python
lista = ["adria", "carla", "joan", "pere", "pere", "carla"]  
#Trobem els valors que no estan repetits i els imprimim 
print(set(lista))  
#Contem el número d'elements a la llista de no repetits i l'imprimim
print(len(set(lista)))
```

### count()
Per contar quantes vegades està un element en una llista (veure exercici 1.7.2 A): .count()

### Per posar límits
- len: llargada de la llista/element
- index: posició a la llista
- append: afegir al final de la llista
- min: selecciona el valor mínim
- max: selecciona el valor màxim
- round: arrodoneix els decimals

### Exercicis 1.7.2
#### Exercici A
La UAB acaba de celebrar sus jornadas de puertas abiertas y los futuros estudiantes han acudido a las sesiones informativas. Cada vez que una persona entra en una sesión se anota su nombre. Alguien ha juntado todos los nombres en una sola lista... ¿Puedes sacar información útil de este listado?
1.  ¿Cuantas personas han asistido a las jornadas de puertas abiertas?
2.  ¿Cuantas personas han asistido a más de dos sesiones?
3. ¿Qué porcentaje de los asistentes accede a más de dos sesiones?

```Python
#A1 Esborrem els repetits i contem  
llista_norep = set(llista)  #creem la llista amb els que no estan repetits
print(llista_norep)  
recompte = len(llista_norep)  #contem quants han repetit
print(f"Hi ha {recompte} alumnes no repetits")  
  
#A3 Busquem repetits i contem  
#opcio1  
repetidors = []  #creem la llista amb els que repeteixen
for nom in llista_norep:  
    contador = llista.count(nom)  
    if contador > 1:  
        repetidors.append(nom)  
numrep = len(repetidors)  
print(f"Hi ha {numrep} repetidors")  
  
#opcio2  
contador = 0  #posem el contador a 0
for nom in llista_norep:  #per a cada nom de la llista sense repetir
    contador2 = llista.count(nom)  #contar quantes vegades està cada nom
    if contador2 > 1:  
        contador = contador + 1  #cada vegada que està repetit se suma un
print(f"Hi ha {contador} repetidors")  
  
#A3 Calcula el percentatge de repetidors
percentatge = 100*(contador/len(llista_norep))  #calculem el percentatge de seguidors
print(f"El percentatge és {percentatge}") #imprimim el percentatge
```


#### Exercici B
1.  Crea un código que imprima, para cada alumno, la nota correspondiente, con el texto "El alumno/a _var_alumnos_ ha obtenido un _var nota_".
2.  Calcula e imprime la nota promedio del aula con un decimal
3.  Calcula e imprime la nota más alta junto al nombre del alumno.
4.  calcula e imprime la nota más baja junto al nombre del alumno.

```Python
#Ens donen les següents llistes
notes = ["5","3","7","8","9.5","4","6,2"]  
alumnes = ["adria","agnès","josep","rafa","cristina","Gemma","Eduard"]  
  
#B1 Imprimim la nota de cada alumne
for nota, alumne in zip(notes, alumnes):  #Juntem les dues llistes amb zip
    print(f"El alumno/a {alumne} ha obtenido un {nota}.")  
  
#B2 Nota promig  
llista_notesbe = []  #primer creem la llista amb les notes netes
for nota, alumne in zip(notes, alumnes): #recorrem totes les notes 
    if "." in nota:  #si hi ha nota amb punt
        notabe = float(nota)  #convertim a float
        llista_notesbe.append(notabe)  #l'afegim com a float 
    elif "," in nota:  #si hi ha nota amb coma la convertim a un punt
        notabe = float(nota.replace(",","."))  
        llista_notesbe.append(notabe)  #i l'afegint com a float
    else:  
        notabe = int(nota)  #si no hi ha cap separador decimal
        llista_notesbe.append(notabe)  #l'afegim com a integer
#imprimim la llista per veure si els canvis estan correctes  
print(llista_notesbe)  
#sumem tots els valors i dividim pel total per fer el percentatge  
nota_final = sum(llista_notesbe)/len(llista_notesbe)  
print(round(nota_final,2))  #imprimim la nota final arrodonint el nombre de decimals que tenim
  
#B3 Imprimir nota més alta amb nom  
notamax = max(llista_notesbe)  #busquem la nota més alta
posicio = llista_notesbe.index(notamax)  #trobem la posició de la nota per poder dir l'alumne
print(f"La màxima és un {notamax}, i l'ha obtingut {alumnes[posicio]}")  #imprimim les dades
  
#B4 Imprimir nota més baixa amb el nom  
notamin = min(llista_notesbe)  #busquem la nota més baixa
posicio = llista_notesbe.index(notamin)  #trobem la posició de la nota per poder dir l'alumne
print(f"La mínima és un {notamin}, i l'ha obtingut {alumnes[posicio]}") #imprimim les dades
```


# Classe 28/02/2023: Diccionaris, Tuples, PANDAS, JSON
## Diccionaris
Són llistes amb parells de valors.
```Python
diccionari = {"clau" : "valor"}
```

## Tupla
Llista dins d'una llista

Exemple:
```Python
#Creem les llistes
llista_1 = [6, 9]  
llista_2 = ["josep", "cristina"]  
llista_final = []  

#Juntem nom i cognom
for nota, nom in zip(llista_1, llista_2):  #unim les llistes en una sola i la recorrem
    conjunt = (nota, nom)  #creem cada entrada en el diccionari
    llista_final.append(conjunt)  #afegim les entrades a la llista final

#Imprimim el nom complet i la nota
for t in llista_final:  #per a cada entrada (persona)
    nota = t[0] #agafem la nota
    nom = t[1] #agafem el nom
    print (nota, nom) #imprimim les dues coses

```

## Introducció a Pandas
**Pandas** és una [llibreria](https://es.wikipedia.org/wiki/Biblioteca_(inform%C3%A1tica) "Biblioteca (informàtica)") de Python especialitzada en la manipulació i l'[anàlisi de dades ](https://ca.wikipedia.org/wiki/An%C3%A1lisis_de_datos "Anàlisi de dades"). Ofereix estructures de dades i operacions per manipular taules numèriques i [sèries temporals](https://es.wikipedia.org/wiki/Series_temporales "Sèries temporals"), és com l'Excel de Python. És un [software lliure](https://es.wikipedia.org/wiki/Software_libre "Software lliure") distribuït sota la [llicència BSD.](https://es.wikipedia.org/wiki/Llicència_BSD "Llicència BSD ")[1](https://es.wikipedia.org/wiki/Pandas_(software)#cite_note-1) El nom deriva del terme "[**da**tos de **pan**el]( https://ca.wikipedia.org/wiki/Dades_de_panel "Dades de panell")" (PANel DAta), terme de [econometria](https://es.wikipedia.org/wiki/Econometr%C3%ADa "Econometria") que designa dades que combinen una dimensió temporal amb una altra dimensió transversal.
Cal instalar i importar aquesta llibreria perquè funcioni: pip install pandas
Pandas read the docs, és la pàgina web per saber-ho tot sobre pandas, per exmple: com podem llegir documents.

### Exercici 1 (Pandas)
```Python
import pandas as pd  
#importem la llibreria pandas per poder exportar-ho tot al final  
  
#Exercici 1: intro a pandas  
#Tenim aquestes llistes  
notes = [1,6,8,9,10,6,5]  
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]  
cognoms = ["Tort","Soldevila","Luna","Muñoz","Fernandez","Hernandez", "Llopart"]  
  
#Tarea 1: Unificar los nombres y apellidos de los alumnos en una única cadena de texto  
#Juntem nom i cognom en una variable  
noms_complets = []  
for alumne, cognoms in zip(alumnes, cognoms):  
    nom_total = (f"{alumne} {cognoms}")  #fem el nom sencer
    noms_complets.append(nom_total)  #afegim a la llista
print(noms_complets)  #imprimim la llista
  
#Tarea 2: Crear una lista de "tuplas" que contengan los datos del alumno unificados, y la nota obtenida  
llista_de_tuples = []  
for nom, nota in zip(noms_complets, notes):  #per a cada element de la llista unificada de noms+notes
    nom_nota = (nom, nota)  #creem un element amb el nom+nota
    llista_de_tuples.append(nom_nota)  
print(llista_de_tuples)  
#Es pot simplificar la tasca en un sol exercici fent el nom complet (tasca 1) dins del for amb un triple zip  
  
#Tarea 3: Sumar un punto a todas la notas, sin que puedan sobrepasar el 10 (i ho volem fer des de les tuples que ja tenim)  
#fem una llista per poder desar totes les dades finals  
llista_definitiva = []  
#fem la tasca 3  
for persona in llista_de_tuples:  
    nova_nota = persona[1]+1  #sumem 1 a la nota de la persona
    if nova_nota > 10:  #si la nota és major a 10
        nova_nota = 10  #la igualem a 10
'''aquí ho podem guardar en una variable així:
	nova_persona = (persona[0], nova_nota)
	print(nova_persona)
o continuar directament amb la tasca 4'''

#Tarea 4: Añadir un tercer elemento a la tupla siguiendo este criterio:  
'''- Si la nota final es inferior a 5, añadir el texto "suspendido".  
- Si la nota se encuentra entre 5 y 6 (ambos incluídos), añadir el texto "aprobado".  
- Si la nota es superior a 6, e inferior a 7, añadir el texto "bien".  
- Si la nota es igual o superior a 7, añadir el texto "notable".  
- Si la nota supera el 9, añadir el texto "Excelente".  
- Si la nota equivale a un 10, añadir el texto "matrícula de honor".  
(ho volem fer agafant l'exercici anterior i posant-ho a dins)  
'''  
#aqui comencem la tasca 4  
    if nova_nota < 5:  #fem un if per a cada condició
        qualificacio = "suspendido"  
    elif 5 >= nova_nota and nova_nota < 6:  #afegim el valor màxim i mínim perquè sinó pot fer coses rares
        qualificacio = "aprobado"  
    elif 6 >= nova_nota and nova_nota < 7:  
        qualificacio = "bien"  
    elif 8 >= nova_nota and nova_nota < 9:  
        qualificacio = "notable"  
    elif 9 >= nova_nota and nova_nota < 10:  
        qualificacio = "excelente"  
    elif 10 == nova_nota:  
        qualificacio = "matrícula de honor"  
    nova_persona = (persona[0], nova_nota, qualificacio)  #juntem tots els apartats per a cada persona
    llista_definitiva.append(nova_persona)  #afegim cada persona a la llista final
print(llista_definitiva)  
  
#Tarea 5: Transforma la lista de tuplas en un dataset.  
#fet al principi del document (linia 1)  
#creem un dataframe (normalment df), osigui una taula
df = pd.DataFrame(llista_definitiva, columns=["nom", "nota", "qualificacio"])  
print(df)  
  
#importem la taula en csv  
df.to_csv("dataset.csv")  
  
#també ho podem importar com a excel (xlsx)  
df.to_excel("dataset.xlsx")  
```

### Llegir documents amb pandas:
Importem documents fàcilment amb pandas.
```Python
#Importem un altre document (exemple.csv)
#na_filter=False és un filtre per exportar False sense tenir errors
df = pd.read_csv("exemple.csv", sep=";", na_filter=False)
print(df)
```

#### .sample
Permet agafar únicament una mostra del dataframe perquè no es peti l'ordinador o perquè no trigui molt de temps en processar les coses.
#### .to_csv
Per exportar el dataframe en un document csv

### Arxius JSON
Obrim, explorem i exportem documents.
--> Ho fem a partir d'un dataset de les condicions que hi havia en l'habitació on es treballa.
```Python
import pandas as pd  
import json  
  
f = open('medidas.json') #carreguem l'arxiu  
data = json.load(f) #i el transformem en diccionaris  
  
#mirem quants elements té el json  
print(len(data))  
  
llista_dades = []  
  
for d in data:  #recorrem cada element (equivalent a la fila de l'arxiu carregat)
    temp = d["temperatura"]  #agafem el valor de la columna temperatura i així amb cada una
    pres = d["presion"]  
    date = d["fecha"]  
    tupla = (temp, pres, date)  #creem una variable "tupla" per tenir tots els valors d'una mateixa fila junts
    llista_dades.append(tupla)  #afegim cada presa de valors a la llista
  
#fem que ho imprimeixi com un dataframe  
df = pd.DataFrame(llista_dades)  
print(df)  
  
#ho volem exportar tot en un document csv  
#ATENCIO que els decimals per obrirlo amb excel han de ser comes  
df.to_csv("temperaturas.csv", index=False, decimal=",")  
  
#en el cas que fos un arxiu molt gran, podem agafar samples (exemples)  
sample = df.sample(frac=0.1)  
sample.to_csv("sample.csv")
```

ATENCIÓ: En l'entorn de python el decimal sempre s'indica amb un punt, però en l'entorn d'excel Espanya amb una coma.


Per trobar la temperatura més alta i la més baixa fem lo següent:
```Python
import pandas as pd  
import json  
  
f = open('medidas.json') #carreguem l'arxiu  
data = json.load(f) #transformar en diccionaris  
  
#mirem quants elements té el json  
print(len(data))  
  
llista_dades = []  
  
for d in data:  
    temp = d["temperatura"]  
    pres = d["presion"]  
    date = d["fecha"]  
    tupla = (temp, pres, date)  
    llista_dades.append(tupla)  
  
df = pd.DataFrame(llista_dades, columns=["temp", "pres", "data"])  
print(df)  
max = df.["temp"].idmax()  #per trobar el valor utilitzem el max
print(df.iloc[[max]]) #per trobar el numero de fila utilitzem idmax i iloc
```


# Classe 07/03/2023: Twitch API
## API Twitch
Entre la base de dades i l'ordinador que ho solicita, hi ha l'API. Mai es comuniquen directament l'ordinador i la BD.
Entrem a PY Twitch API (https://pytwitchapi.readthedocs.io/en/v2.5.7/index.html) Aquesta web ens explica com utilitzar la llibreria per simplificar el codi necessari per consultar l'API des de l'ordinador. Fa d'intermediari entre API i ordinador.
També consultem la web dels apunts: https://adriapadilla.github.io/bigdata-uab/twitch.html

### pip install
Copiem el següent text al terminal de l'ordinador/PowerShell/Pycharm (segons com ho tinguem configurat) per instalar la llibreria:
```Python
pip install twitchAPI==2.5.7.1
```

### .sleep
Afegim .sleep perquè trigui més en demanar a l'API i així no arribi al límit i ens veti l'accés.

### Continuem amb l'exercici
Ja està instalada la llibreria i ara entrem amb les claus que hem creat desde la web de desenvolupadors de Twitch: https://dev.twitch.tv/
```Python
from twitchAPI.twitch import Twitch
from pprint import pprint
twitch = Twitch('my_app_key', 'my_app_secret')
pprint(twitch.get_users(logins=['your_twitch_username']))
```

Fem proves i tractem dades.
Per crear un document amb les dades obtingudes utilitzem el següent codi extret del github:
```Pyhton
with open("output_file.json", 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
```

Netegem les dades.
Creem un df i l'exportem
```Python
#importem la llibreria de twitch  
from twitchAPI.twitch import Twitch  
  
#importem json per poder llegir-crear docus json  
import json  
  
#importem datetime per saber quina hora és  
import datetime  
now = datetime.datetime.now()  
  
#importem pandas  
import pandas as pd  
  
#aquí fem l'accés al compte de twitch i l'aplicació que hem creat abans a dev.twitch (llibreria twitch)  
twitch = Twitch('aquí va el meu identificador', 'aquí va la meva clau')  
  
#obtenim els streams que volem (seleccionem perquè sinó peta el ordinador) 
streams = twitch.get_streams(first=20, language='es')  
  
#hem obert "streams" i hem vist que el que ens interessa obtenir és "data"  
dades = streams["data"]  
  
#per juntar els dataframes del for creem la següent llista buida  
llista_dataframes = []  
  
#agafem únicament les dades que volem, les netegem  
for dada in dades:  
    captured_at = now  
    user_id = dada["user_id"]  
    user_name = dada["user_name"]  
    game_id = dada["game_id"]  
    game_name = dada["game_name"]  
    title = dada["title"]  
    viewer_count = dada["viewer_count"]  
    started_at = dada["started_at"]  
    is_mature = dada["is_mature"]  
  
#creem un dataframe per a cada stream  
    df = pd.DataFrame({  
        "captured_at": captured_at,  
        "user_id": user_id,  
        "user_name": user_name,  
        "game_id": game_id,  
        "game_name": game_name,  
        "title": title,  
        "viewer_count": viewer_count,  
        "started_at": started_at,  
        "is_mature": is_mature,  
    }, index=[0])  
  
#afegim un stream en dataframe darrere un altre en una mateixa llista  
    llista_dataframes.append(df)

#juntem tots els streams per a que es crei una sola taula  
final_dataframe = pd.concat(llista_dataframes)
#exportem el dataframe en un csv sense índex a la primera columna  
final_dataframe.to_csv("export.csv", index=False)
```

## Variables i funcions
Apliquem variables  i funcions.
```Python
variable2 = "hola"  
  
def loquesea(var):  
    print(var)  
  
loquesea(variable2)
```

Mirem de treure les dades amb variables i funcions, fent-ho també en català i castellà.
```Python
#importem la llibreria de twitch  
from twitchAPI.twitch import Twitch  
  
#importem json per poder llegir-crear docus json  
import json  
  
#importem datetime per saber quina hora és  
import datetime  
now = datetime.datetime.now()  
  
#importem pandas  
import pandas as pd  
  
import time  
  
#aquí fem l'accés al compte de twitch i l'aplicació que hem creat abans a dev.twitch (llibreria twitch)  
twitch = Twitch('aquí va el meu identificador', 'aquí va la meva clau')  
  
llista_dataframes = [] #per juntar els dataframes del for creem la següent llista buida  
idiomes = ["es", "ca"] #per trobar els dos idiomes establim la variable  
cursor_dummy = None #establim cursor perquè estigui definida la variable cursor per la primera iteració. Cursor i pagination ens permeten obtenir més pàgines de dades de la API
  
def crida(cursor, lang):  #definim la funció
    #obtenim els streams que volem  
    streams = twitch.get_streams(first=100, language=idiomes, after=cursor)  
  
    #hem obert "streams" i hem vist que el que ens interessa obtenir és "data"  
    dades = streams["data"]  
  
    #agafem únicament les dades que volem del dataset
    for dada in dades:  
        captured_at = now  
        user_id = dada["user_id"]  
        user_name = dada["user_name"]  
        game_id = dada["game_id"]  
        game_name = dada["game_name"]  
        title = dada["title"]  
        viewer_count = dada["viewer_count"]  
        started_at = dada["started_at"]  
        is_mature = dada["is_mature"]  
  
        #creem un dataframe per a cada stream  
        df = pd.DataFrame({  
            "captured_at": captured_at,  
            "user_id": user_id,  
            "user_name": user_name,  
            "game_id": game_id,  
            "game_name": game_name,  
            "title": title,  
            "viewer_count": viewer_count,  
            "started_at": started_at,  
            "is_mature": is_mature,  
        }, index=[0])  
  
        #afegim un stream darrere un altre en una mateixa llista  
        llista_dataframes.append(df)  
  
    print(len(llista_dataframes))  
  
    try:  #fem un try perquè sinó quan arriba a l'última pàgina dona error i es para el programa
        cursor = streams ["pagination"]["cursor"]  #agafem pagination i cursor de la llista d'streams per poder extreure diferents pàgines
        print(f"Fent una nova consulta. Idioma: {lang} - Total streams: {len(llista_dataframes)}")  #imprimim contingut per saber l'estat
        time.sleep(0.12)  #afegim sleep perquè la API no arribi al límit i ens veti l'accés
        crida(cursor, lang)  
    except KeyError:  #quan salti aquest error sabem que serà per l'última pàgina
        print("Última pàgina")  
        pass  
  
for lang in idiomes:  #iterem per fer el procés anterior anomenat "crida" per als dos idiomes
    crida(cursor_dummy, lang)  
  
#juntem tots els streams per a que es creï una sola taula  
final_dataframe = pd.concat(llista_dataframes)  
#exportem el dataframe en un csv sense índex a la primera columna  
final_dataframe.to_csv("export.csv", index=False) 
#també el podem imprimir en pantalla però si hi ha moltes files o columnes, només imprimirà una part
print(final_dataframe)
```


# Classe 14/03/2023: Pandas (YT i Twitch)
## Exercici 2 pandas
### .drop / .pop
Per treure elements del dataframe, podem utilitzar drop i pop. Les dues opcions son bones, però drop és millor perquè és natiu de pandas.
Perquè les columnes s'esborrin realment de la variable actual cal crear una nova variable o utilitzar inplace=True. Depèn del que volguem fer després per utilitzar un o altre, depen si volem recuperar després el primer dataframe.

### .mean
Permet calcular la mitjana dels valors: (suma del total) / (numero de valors).
Molt útil per calcular la mitjana d'una llista per exemple.

### .iterrows
Recorre totes les files del DF que li demanem.
Exemple més avall en  l'Ex.2: Dataset Youtube.

### .loc
Localitza i selecciona elements dins d'una columna. També pot ser un rang, un nom, un numero concret... Per exemple, selecciona les files que tenen com a titol NPR Music.
```Python
df_1 = df.loc[df['channelTitle'] == "NPR Music"]
```


## Exercici 2: Dataset YouTube
Provisional correcció exercici 2 (a mig corregir)
```Python
import pandas as pd  
#importem la llibreria  
  
#1. importem el dataset en un dataframe  
df = pd.read_csv("dataset_youtube.csv", sep=",", na_filter=False)  
print(df)  
  
  
#2. imprimim el numero de files i columnes  
print(f"Les files i columnes són: {df.shape}")  
''' Així ho vaig fer jo però és més òptim de l'atre manera  
fil = len(ds)  
col = len(df.columns)  
print(f"Hi ha {col} columnes i {fil} files.")'''  
  
  
#3. Mostrem les columnes del dataset  
nombre_columnas = df.columns  
for col in nombre_columnas:  
    print(col)  
  
  
#4. Limpia los datos, si es necesario  
#No cal fer aquesta neteja de moment  
  
  
#5. Elimina columnas, si es necesario  
df.drop(["position","publishedAt","dislikeCount","channelId"], axis=1, inplace=True)  
print(df.shape)  
  
  
#6. Calcula cuantos vídeos ha publicado cada canal  
#mirem quans canals hi ha  
canals_unics = df.channelTitle.unique()  
print(canals_unics)  
#creem un dataframe per a cada canal  
df_1 = df.loc[df['channelTitle'] == "NPR Music"]  
df_2 = df.loc[df['channelTitle'] == "KEXP"]  
print(f'Hi ha {df_1.shape[0]} vídeos a NPR Music')  
print(f'Hi ha {df_2.shape[0]} vídeos a KEXP')  
  
  
#7. Calcula el promedio de espectadores/comentarios/likes que tiene cada uno de los canales  
#per a cada canal i variable fem el calcul i arrodonim en dos  
#viewers  
print(f'Hi ha {round(df_1["viewCount"].mean(), 2)} viewers a NPR Music') #mean permet calcular la mitjana dels valors 
print(f'Hi ha {round(df_2["viewCount"].mean(), 2)} viewers a KEXP')  
#comentaris  
print(f'Hi ha {round(df_1["commentCount"].mean(), 2)} comentaris a NPR Music')  
print(f'Hi ha {round(df_2["commentCount"].mean(), 2)} viewers a KEXP')  
#likes  
print(f'Hi ha {round(df_1["likeCount"].mean(), 2)} comentaris a NPR Music')  
print(f'Hi ha {round(df_2["likeCount"].mean(), 2)} viewers a KEXP')  
  
#8. Calcula la desviación de cada vídeo sobre el promedio de especatadores/comentarios/likes  
#viewers  
list_desviacio = []  

#calculem els promigs d'espectadors
prom_expectadors_1 = round(df_1["viewCount"].mean(), 2)  
prom_expectadors_2 = round(df_1["viewCount"].mean(), 2)  

for index, row in df_1.iterrows()  #per a cada parell de valors de cada llista del df dins de la iteració per files
    desviacio = prom_expectadors_1 - row["viewCount"]  #calcula amb la fómrula la desviació


'''
Aquests altres exercicis ja no els vam arribar a fer ni corregir:
#9. Localiza el vídeo más visto de cada canal  
#10. Localiza el vídeo más comentado de cada canal'''
```

## Continuació classe nou exercici twitch dataset gran (mida: 4G)
### Separadors datset
Utilitzarem "\\t" perquè aquest dataset està separat per tabuladors.

### Agafem una mostra perquè sinó peta
- Nrows: serveix per carregar només una selecció de files.
- Usecols: per carregar només una selecció de columnes.
- Chunksize: Agafa el df i el divideix en blocs de les files que indiquem per anar-les processant per blocs i que no exploti l'ordinador.

Volem saber la durada del stream.
```Python
import pandas as pd  
import time  
  
#columnes en el dataset  
inici = time.time()  

#utilitzarem \t perquè aquest dataset està separat per tabuladors  
#Per estalviar temps de càrrega utilitzarem nrows i usecols.  
df = pd.read_csv("feb-full-2023.csv",  
                 sep='\t',  
                 nrows=2  
                 usecols=["captured_at","streamer_name","viewer_count","game_name","stream_title"])  
print(df)  
  
for col in df.columns:  #imprimim els noms de les columnes
    print(col)  
  
final = time.time()  
print(final-inici)
```

Volem veure quin ha estat el directe amb el pic més alt de visualitzacions.
```Python
import pandas as pd  
import time  
  
#columnes en el dataset  
inici = time.time()  
  
#utilitzarem \t perquè aquest dataset està separat per tabuladors  
#Per estalviar temps de càrrega utilitzarem nrows i usecols.  
df = pd.read_csv("feb-full-2023.csv",  
                 sep='\t',  
                 nrows=10000,  
                 usecols=["captured_at","streamer_name","viewer_count","game_name","stream_title"])
print(df)  
  
#per veure quines columnes tenim en el df  
for col in df.columns:  
    print(col)  
  
  
#mirem en quina posició està el stream amb més viewers  
posicio = df["viewer_count"].idmax()  
#printem les característiques que volem d'aquell stream  
print(df["captured_at"].iloc[posicio],df["streamer_name"].iloc[posicio],df["stream_title"].iloc[posicio], df["viewer_count"].iloc[posicio])
```

Treballarem únicament amb les dades de la kingsleague i exportem
```Python
import pandas as pd  
import time  
  
#columnes en el dataset  
inici = time.time()  
  
#utilitzarem \t perquè aquest dataset està separat per tabuladors  
#Per estalviar temps de càrrega utilitzarem nrows i usecols.  
df = pd.read_csv("feb-full-2023.csv",  
                 sep='\t',  
                 nrows=1000000000,  
                 usecols=["captured_at","streamer_name","viewer_count","game_name","stream_title"],  
                 chunksize=100000)  
#chunksize ens divideixen el dataframe en fragments i ens el converteix en llistes  
print(df)  
  
llista_kings_leage = []  
  
for chunk in df:  #processem els chunks un per un per estalviar recursos de l'ordinador
    dades_kings_leage = chunk[chunk["streamer_name"] == "kingsleague"] #afegim a una nova llista cada chunk que tingui el nom d'streaming kingsleage 
    print(dades_kings_leage)  #imprimim la llista per controlar el procés
    llista_kings_leage.append(dades_kings_leage)  #afegim els elements a la llista final
  
final_frame = pd.concat(llista_kings_leage)  #juntem les llistes en un sol DF
final_frame.to_csv("kingsleague.csv", index=False) #exportem el DF final a csv
```


# Classe 21/03/2023: API Spotify
## Exercici API spotify
Direccions d'on treiem les dades i on explica en general el que fem.
Explicació apunts de classe: https://adriapadilla.github.io/bigdata-uab/spotify.html
Explicació readthedocs: https://spotipy.readthedocs.io/en/2.22.1/#
Explicació API SPotify: https://developer.spotify.com/

Utilitzarem una llibreria (Spotipy) per utilitzar la API com en l'anterior exercici de l'API de Twitch.

### .dump
Ens serveix dins del codi per convertir dataframes o llistes a documents com JSON.

Comprobem els coneixements bàsics i que ens funciona.
```Python
import spotipy  
from spotipy.oauth2 import SpotifyClientCredentials  #codi que hem copiat per importar la llibreria
import json  
  
#aquí hem de copiar l'ID i la clau que genera la web developer de Spotify 
SPOTIPY_CLIENT_ID='el-meu-id' 
SPOTIPY_CLIENT_SECRET='la-meva-clau'  
  
auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET)  
sp = spotipy.Spotify(auth_manager=auth_manager)  
  
playlist = "37i9dQZF1DZ06evO2JsOr8"  #introduim el ID de la playlist sobre la que volem obtenir les dades (codi final de la URL). La playlist en aquest cas és "This is Bad Gyal".

#Utilitzem la web següent per extreure el codi per tractar la playlist:
#https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.playlist_items  
  
query = sp.playlist_items(playlist, fields=None, limit=100, offset=0, market=None, additional_types=('track', 'episode'))  #Posem tota la petició d'informació de la playlist en una llista

with open('hola.json', 'w', encoding='utf-8') as f:  #posem tota aquesta info en un json
    json.dump(query, f, ensure_ascii=False, indent=4) #utilitzem .dump per tractar la info i convertir-la en un document
```

Exportem les llibreries, extraiem les dades i ho exportem en un csv per poder manipular i visualitzar les dades.
```Python
#importem les llibreries
import spotipy  
from spotipy.oauth2 import SpotifyClientCredentials  
import json  
import time  
import pandas as pd  

#copiem el codi d'accés a la API d'Spotify
SPOTIPY_CLIENT_ID = 'el-meu-id'  
SPOTIPY_CLIENT_SECRET = 'la-meva-clau'  
auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)  
sp = spotipy.Spotify(auth_manager=auth_manager)  

#establim la playlist sobre la que volem treballar
playlist = "3oopyXIZGLFtHjFYN9KbuI"  

#en cas de dubte podem consultar el readthedocs de spotipy
# https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.playlist_items  

#creem la petició d'info de la playlist
query = sp.playlist_items(playlist, fields=None, limit=100, offset=0, market=None,  
                          additional_types=('track', 'episode'))  
  
relacions = []  
  
for i in query["items"]:  #la llista de items hem vist que és la llista de cançons
    artists = i["track"]["artists"] #Al ser una llista i no un claudàtor hem d'iterar tots els elements. Agafem la llista d'artistes de la cançó
    for artist in artists:  #per a cada artista treiem només nom i ID
        source_artist_name = artist["name"]  
        source_artist_id = artist["id"]  
        #print(source_artist_name,source_artist_id)  #printem si volem comprovar que funciona correctament
  
        try:  #utiltzem try perquè sino el programa no correria fins al final
            related_artists = sp.artist_related_artists(source_artist_id)  #obtenim els artistes relacionats de la llista d'artistes que apareixen a la playlist
            relacionats = related_artists["artists"]  #agafem només el mon de l'artista
            for l in relacionats:  
                related_artist_name = l["name"] #recorrem la llista d'artistes relacionats i els afegim en una llista  
                tupla = (source_artist_name,related_artist_name) #Ara afegim en tuples totes les relacions  
                relacions.append(tupla) #ho afegim a la llista final 
            print("Etic dormint")  #cprintem per controlar les iteracions
            time.sleep(1)  #parem el programa per no arribar al límit de peticions de la API i que ens bloquegi
  
        except TypeError:  #quan salti l'error, voldrà dir que ja no hi ha més items
            pass  #per tant l'ignorem
  
df = pd.DataFrame.from_records(relacions, columns=['source','target'])  #creem un dataframe amb la tupla "relacions", amb dues columnes anomenades source i target
df.to_csv("dataset.csv", index=False) #exportem a csv
```


# 28/03/2023: Exercici Pandas i treball final
Exercici de classe pandas
```Python
import pandas as pd
#opcio 1: opció bona però potser no funciona amb df molt grans
df = pd.read_csv("feb_23_es_simple.csv", sep="\t", usecols=["captured_at", "viewer_count"]) #obrim el document per llegir-lo carregant només les columnes que volem utilitzar perquè no es peti l'ordinador.
df2 = df.groupby("captured_at")["viewer_count"].sum()reset_index() #groupby ens permet agrupar per les dates que son iguals, i llavors .sum suma els valors de "viewer count"
df2.to_csv("test.csv") #guardem el df en un csv

#opcio 2: per chunks, més òptima, especialment per a grans quantitats
df = pd.read_csv("feb_23_es_simple.csv", chunksize=10000, sep="\t", usecols=["captured_at","viewer_count"] #agafem només alguns elements seleccionats amb el chunksize
for chunk in df:
	df2 = chunk.grupby("captured_at")["viewer_count"].sum()reset_index() #resetindex ens permet que l'índex no s'esborri, perquè sinó tindríem la data en l'índex enlloc d'una columna 

final_frame_1 = pd.concat(list)
final_frame_2 = final_frame_1.groupby("captured_at")["viewer_count"].sum()
final_frame_2.to_csv("test_2.csv")

```