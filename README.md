# ITALIANO

# Blender-Case
Fatto e testato con Blender versione 2.81

# Nel file dado-case-2.81.blend 

# CasetteMatrice.py
Crea un "castello" leggendo i dati da 2 vettori, uno per le altezze delle costruzioni e uno per i tipi di tetto.
I tetti sono costruiti usando i dati dei vertici.
Le texture delle case sono lette dalla sotto-directory "texture" una per colore e una per far trasparire il colore random del materiale.
Esiste una copia di texture per il primo piano e una per il secondo e terzo piano.
Cambiando i valori in MH potete cambiare l'altezza delle case (= 0 non c'è la casa e da 1 fino a 3 piani)
Cambiando i valori in MT potete cambiare il tipo di tetto (valori da 1 a 8)

# CasetteRandom.py
Crea una città con tipi di case da 1 a 3 piani (0 non fa niente)
Cambiando i valori NX e NY cambia le dimensioni della "città"
Il valore DC determina la distanza tra le case.

# CreaPath.py
Crea un path per abbinare a una camera, adatto per il "castello" creato da CasetteMatrice.py

# file dado-case-2.81.blend
La camera abbinata al percorso.

# ENGLISH

# Blender-Case
Made and tested with Blender version 2.81

# In the dado-case-2.81.blend file

# CasetteMatrice.py
Create a "castle" by reading data from 2 vectors, one for building heights and one for roof types.
Roofs are constructed using data from the vertices.
The textures of the houses are read from the sub-directory "texture" one for color and one to show the random color of the material.
There is a copy of the texture for the first floor and one for the second and third floor.
By changing the values in MH you can change the height of the houses (= 0 there is no house and from 1 to 3 floors)
By changing the values in MT you can change the type of roof (values from 1 to 8)

# CasetteRandom.py
Create a city with house types from 1 to 3 floors (0 does nothing)
Changing the NX and NY values changes the size of the "city"
The DC value determines the distance between the houses.

# CreaPath.py
Create a path to match a room, suitable for the "castle" created by CasetteMatrice.py

# dado-case-2.81.blend file
The camera combined with the path.
