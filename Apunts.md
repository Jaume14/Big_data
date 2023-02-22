#prova
# Títol 1 (# )
## Títol 2 (## )
### Títol 3 (### )
...
Text normal

```
Això és un text de codi i s'ha d'obrir amb (```)
```

## PyCharm
Perquè pycharm? Perquè utiilitza un entorn virtual perquè no hi hagi problemes amb la versió del Python (que a cada ordinador de classe pot haver-hi instalada una versió diferent)

## Remember Python
### Cadena de text
Liada amb cometes
--> Utilitzar simples/dobles
Els dos exemples són cadenes de text.
``` "cadena de text" 'cadena de text' ```

### Print
--> Mostrar a pantalla el que sigui
--> separar amb comes els diferents tipus de coses:
```"L'usuari", usuari, "té", likes, "likes."```

### Numeros
--> Integers: sense punt 1
--> Float: amb punt 1.2
--> Per passar de string a integer: int(numero_string)
```Python
for n in notas:  
    nota_numerica = int(nota)
```

### Variables
--> Text directament escrit amb un igual al final: variable = 1

### Pycharm
--> Ctrl + L neteja pantalla
--> Ctrl + C aturar procés

### Funcions
#### str
--> Uneix diferents tipus de dades en un string:
```frasestring = str"L'usuari "+usuari +"té" +likes +"likes."```

### Propietats
--> Les variables es poden sobreescriure, la que mana és la última per ordre de lectura del text.
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
```llista_tots_alumnes = [llistanoms, Maria, Pere, Paula]```
Per afegir elements a les llistes .append o .extend
```Python
llista_noms = llista_noms.append(nou_nom)
```

# 21/02/2023
## Bucles For/If

```Python
llista_noms = ["carme", "joan"]  
  
for nom in llista_noms:  
    if nom == "joan":  
        print(nom)  
    else:  
        print(nom + " no és en Joan")
```

Per fer més eficient el bucle, es pot utilitzar f{nom}
```Python
llista_noms = ["carme", "joan"]  
  
for nom in llista_noms:  
    if nom == "joan":  
        print(nom)  
    else:  
        print(f"{nom} no és en Joan")
```

Si hi ha més condicions intemitges utilitzem elif
```Python
numeros = [1,2,3,6,7,8,10,15]  
  
for n in numeros:  
    if n<6:  
        print(f"{n} és menor que 6")  
    elif n==6:  
        print(f"{n} és igual que 6")  
    else:  
        print(f"{n} és major que 6")
```

## Funcions natives de Python
Per exemple print.

Per veure com de llarga és la llista len
```Python
numeros = [1,2,3,6,7,8,10,15]
print(len(numeros))
```

Per aparellar llistes d'un amb un altre: zip().
--> Veure exercici B


Exercici A
```Python
txt = "esto es un ejercicio"  
print(txt)  
  
  
nota = 10  
asignatura = "BigData"  
  
txt1 = f"En la asignatura {asignatura} he obtenido un {nota}"  
print(txt1)  
  
nota = 5  
txt1 = f"En la asignatura {asignatura} he obtenido un {nota}"  
print(txt1)
```

Exercici B
```Python
#Un compañero te ha mandado dos listados: las notas y los nombres de los alumnos a quienes corresponden dichas notas:  
notas = ["5","7","6","4","8","2"]  
alumnos = ["jaume","carla","pere","adrià","rafael","agnès"]  
  
for nota, nom in zip(notas, alumnos):  
    nota_numerica = int(nota)  
#Debes sumar 1 punto a cada una de las notas.  
    nota_final = nota_numerica + 1  
#Imprime el resultado junto al nombre del correspondiente alumno de tal manera que: "var_alumno ha obtenido un var_nota".  
    print(f"{nom} ha obtenido un {nota_final}")
```

Per veure la posició d'un element en una llista
```Python
llista = ["adria", "carla", "joan", "pere"]  
nom = "joan"  
if nom in llista:  
    print("si")  
    position = llista.index(nom)  
    print(position)  
else:  
    print("no")
```

Per esborrar valors repetits set()
```Python
lista = ["adria", "carla", "joan", "pere", "pere", "carla"]  
#Trobem els valors que no estan repetits i els imprimim 
print(set(lista))  
#Contem el número d'elements a la llista de no repetits i l'imprimim
print(len(set(lista)))
```

Per contar quantes vegades està un element en una llista (veure exercici 1.7.2 A): .count()

Per posar límits

len
index
append
min
max

### Exercicis 1.7.2
#### Exercici A
La UAB acaba de celebrar sus jornadas de puertas abiertas y los futuros estudiantes han acudido a las sesiones informativas. Cada vez que una persona entra en una sesión se anota su nombre. Alguien ha juntado todos los nombres en una sola lista... ¿Puedes sacar información útil de este listado?
1.  ¿Cuantas personas han asistido a las jornadas de puertas abiertas?
2.  ¿Cuantas personas han asistido a más de dos sesiones?
3. ¿Qué porcentaje de los asistentes accede a más de dos sesiones?

```Python
#A1 Esborrem els repetits i contem  
llista_norep = set(llista)  
print(llista_norep)  
recompte = len(llista_norep)  
print(f"Hi ha {recompte} alumnes no repetits")  
  
#A3 Busquem repetits i contem  
#opcio1  
repetidors = []  
for nom in llista_norep:  
    contador = llista.count(nom)  
    if contador > 1:  
        repetidors.append(nom)  
numrep = len(repetidors)  
print(f"Hi ha {numrep} repetidors")  
  
#opcio2  
contador = 0  
for nom in llista_norep:  
    contador2 = llista.count(nom)  
    if contador2 > 1:  
        contador = contador + 1  
print(f"Hi ha {contador} repetidors")  
  
#A3 Calcula el percentatge  
percentatge = 100*(contador/len(llista_norep))  
print(f"El percentatge és {percentatge}")
```


#### Exercici B
1.  Crea un código que imprima, para cada alumno, la nota correspondiente, con el texto "El alumno/a _var_alumnos_ ha obtenido un _var nota_".
2.  Calcula e imprime la nota promedio del aula con un decimal
3.  Calcula e imprime la nota más alta junto al nombre del alumno.
4.  calcula e imprime la nota más baja junto al nombre del alumno.

```Python
notes = ["5","3","7","8","9.5","4","6,2"]  
alumnes = ["adria","agnès","josep","rafa","cristina","Gemma","Eduard"]  
  
#B1 Imprimim la nota de cada alumne  
for nota, alumne in zip(notes, alumnes):  
    print(f"El alumno/a {alumne} ha obtenido un {nota}.")  
  
#B2 Nota promig  
llista_notesbe = []  
for nota, alumne in zip(notes, alumnes):  
    if "." in nota:  
        notabe = float(nota)  
        llista_notesbe.append(notabe)  
    elif "," in nota:  
        notabe = float(nota.replace(",","."))  
        llista_notesbe.append(notabe)  
    else:  
        notabe = int(nota)  
        llista_notesbe.append(notabe)  
#imprimim la llista per veure si els canvis estan correctes  
print(llista_notesbe)  
#sumem tots els valors i dividim pel total per fer el percentatge  
nota_final = sum(llista_notesbe)/len(llista_notesbe)  
print(round(nota_final,2))  
  
#B3 Imprimir nota més alta amb nom  
notamax = max(llista_notesbe)  
posicio = llista_notesbe.index(notamax)  
print(f"La màxima és un {notamax}, i l'ha obtingut {alumnes[posicio]}")  
  
#B4 Imprimir nota més baixa amb el nom  
notamin = min(llista_notesbe)  
posicio = llista_notesbe.index(notamin)  
print(f"La mínima és un {notamin}, i l'ha obtingut {alumnes[posicio]}")
```

