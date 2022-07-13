# Evaluacion
### Paso 1 Crear un ambiente virtual 
En linea de comandos ejecutar lo sigueinte 
`python3 -m venv env`
###Paso 2 Activar el ambiente virutal 
En linea de comandos ejecutar lo sigueinte 
`source env/bin/activate`
###Paso 3 Instalar dependencias 
Una vez que el ambiente este activado ejecutar el siguiente comando 
`pip install  requirenments.txt`
###Paso 4 Activar el api 
Con el siguente comando activamos el api
`uvicorn app:app --reload`
### Paso 5 Abrir una nueva terminal
En la nueva terminal ejecutamos el paso 2 y probamos el CLI de la siguiente manera 
` python main.py alberto 123`