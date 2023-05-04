# A. Anàlisi general amb Tableau  
Les dades extretes corresponen als tweets en què apareixen els alcaldables de les eleccions municipals de Barcelona 2023. El període de captació compren entre el dia 1 d'abril de 2023 a les 00:00h fins al dia 16 d'abril a les 23:59h.

## Evolució temporal

![[Pasted image 20230427173123.png]]

En l'anàlisi temporal del nombre de tweets, podem veure que l'acumulació per hora fluctua al llarg del període estudiat. Els dies 3 i 4 d'abril hi ha un pic que gairebé arriba als 800 tweets per hora. Aquest augment podria ser degut a la publicació oficial en el BOE d'aquestes eleccions, entre altres motius. La resta de dies, el nombre de tweets per hora és força constant, amb un augment puntual alguns dies (11, 12, 15, 16), però el pic inicial arriba a quadruplicar la resta.  
També es pot observar una tendència diària cíclica, que s'amplia a continuació.

![[Pasted image 20230427173012.png]]

Analitzant més en concret el recompte de tweets per hora del dia, es pot observar el moviment cíclic diari de l'altre gràfic. Hi ha un període vall a partir de les 22h fins a les 6h, en què l'acumulació de tweets per hora disminueix dels 1500 fins a arribar al mínim cap a les 2h, en què no se superen els 250 tweets.  
Durant el matí i fins a les 15h és quan es produeixen la majoria de tweets. Es produeixen dos pics, a les 8h i a les 13h. Probablement, ambdós pics corresponen al moment d'entrada-sortida de la feina i moment de menjar, primer el d'esmorzar i després el de dinar. A la tarda disminueix el nombre de tweets. Però abans de caure en el període vall, es pot observar un repunt cap a les 20h que probablement correspondrà a l'hora de sopar.  
Cal destacar que els moments en els quals es produeix un augment, és també abans dels àpats. Caldria fer una investigació més profunda per concretar el motiu, però també cal tenir en compte que és un moment en què els usuaris tenen més temps lliure i que és l'hora dels informatius.

## Recompte de tweets

![[Pasted image 20230504130356.png]]  
![[Pasted image 20230504132825.png]]

Comparant el nombre de tweets per usuari en aquest període hi ha certs usuaris que són molt actius. Els primers de la llista es troben molt separats de la resta d'usuaris, que majoritàriament han fet un tweet.

![[Pasted image 20230504131032.png]]

En aquest gràfic podem observar els que han fet més de 40 tweets en el període estudiat. La majoria de perfils han estat força actius de manera constant i cada vegada més. Però podem observar grans pics com el de JuanCar02750425, un perfil crític amb l'esquerra política i nacionalista de l'Estat Espanyol. La resta d'usuaris tenen pics i valls, però publiquen més d'un dia majoritàriament.

## Nombre de tweets respecte d'impressions

![[Pasted image 20230427173644.png]]

En comparar el nombre de tweets amb les impressions, podem veure que els usuaris amb més tweets no acostumen a tenir la repercussió corresponent, a excepció de btvnoticies. La majoria es concentra per sota els 10 tweets i les 50K impressions. Destaca la posició dels usuaris amb més seguidors (representats per la mida del punt), ja que gairebé tots són perfils de premsa. Els usuaris que aconsegueixen més repercussió en impressions són: el_pais, btvnoticies, elmundoes i FroiLannister.

## Perfils oficials dels alcaldables

![[Pasted image 20230427175228.png]]

En relació amb els perfils oficials dels candidats, es pot observar que PareraEva és la més activa i que els que obtenen més impressions són: annagrauarias, danielsirera i ernestmaragall.

Ada Colau és l'alcaldable més mencionada, tot i que no utilitza el seu perfil per fer cap publicació des del 2021, en què va anunciar que deixava Twitter de manera indefinida. Tot i això, és la més mencionada i per poder comparar la resta de candidats cal fer una taula sense ella i així poder veure les modificacions que es produeixen al llarg del temps.

![[Pasted image 20230504133612.png]]

L'evolució de les mencions a Ada Colau supera el pic dels 4K de tweets en què se la menciona. Darrere seu, podem observar que Trias arriba a un pic de 600 tweets, Parera als 400 i change als 300. La resta de candidats tenen unes mencions inferiors.

![[Hoja 11.png]]

# B. Anàlisi de les comunitats amb Gephi

## Visió general per grau d'entrada  
Per a l'anàlisi s'ha generat un graf de comunitats amb Gephi. Es poden observar les comunitats d'usuaris representades amb diferents colors, així com la seva vinculació a través de la proximitat dels nodes. La mida dels nodes correspon al nombre d'usuaris que el mencionen (grau d'entrada). Hi ha comunitats molt relacionades, així com d'altres que es troben molt més distanciades, però no observem cap comunitat important que sigui una illa totalment aïllada. Principalment, trobem dues comunitats, la de la dreta (vermell, blau i verd) i la de l'esquerra (rosa, taronja i lila).

![[Pasted image 20230504134006.png]]

### Comunitat reaccionària  
En general, al grup de la dreta trobem una comunitat contrària a AdaColau, vinculada a l'extrema dreta i l'espanyolisme. Els tuits acostumen a ser crítiques poc constructives i sovint força dures. La comunitat és activa i amb contingut reaccionari. Al voltant del node vermell trobem a l'usuari WillyTolerdoo, l'usuari al qual mencionen més. Es pot comprovar que hi ha tota una comunitat força aïllada de la resta que el menciona, tot i que també hi ha una minoria que s'inclou dins de les altres comunitats. FroiLannister, capTercio, ivanedim i ToroenReposo segueixen una tendència semblant, tot i que les seves comunitats estan més entrellaçades.

![[Pasted image 20230504102654.png]]

### Comunitat política  
La comunitat que queda agrupada al cantó esquerre del gràfic està molt més relacionada a un entorn polític. Hi ha perfils oficials com partits polítics o comptes de premsa. Tot i que la crítica i el debat polític també apareix, és d'una forma generalment més respectuosa o constructiva. Destaquen certs usuaris, com OnVasBarcelona i Eduardo54812683, opositors a Ada Colau.

![[Pasted image 20230504103055.png]]

## Visió general per grau de sortida  
En canvi, si es fa el gràfic tenint en compte l'origen de la menció, trobem que els usuaris estan molt més repartits. Tot i que també trobem certs nodes que destaquen sobre els altres, ja sigui pel volum de mencions que fan (mida) o per la vinculació amb altres grups (colors).

![[Pasted image 20230504105004.png]]

Trobem usuaris que mencionen molt i, per tant, el seu node és més gran: ander_the_table, vadortitus, DespertaFerro11, Eduardo54812683 o LauraMartiBCN. Però de totes maneres, els usuaris es troben molt concentrats en el centre, ja que els usuaris que mencionen, no ho fan exclusivament cap a un altre usuari, sinó que en mencionen a diferents, el que crea una xarxa molt densa.

![[Pasted image 20230504105130.png]]

### Comunitat de WillyTolerdoo  
Sorprèn el cas d'alguns usuaris que actuen de hub com WillyTolerdoo o Eduardo54812683. WillyTolerdoo es troba a la part inferior dreta en blau i els usuaris que apareixen són la seva comunitat. És un usuari que menciona poc, però és molt mencionat per gran part d'usuaris. Hi ha una comunitat que el menciona que no està relacionada amb cap altra i que queda molt llunyana del centre.

![[Pasted image 20230504105303.png]]

### Comunitat d'Eduardo54812683  
Eduardo54812683 té una situació semblant tot i que amb un nombre de mencions molt inferior. És un usuari que menciona molt, però no és mencionat de manera corresponent. Tot i això, els usuaris que ho fan, es troben al centre del gràfic, però també n'hi ha que estan aïllats i que no mencionen a ningú més.

![[Pasted image 20230504105651.png]]

