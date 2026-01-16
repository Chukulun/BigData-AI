#En este segundo caso vamos a ejecutar directamente el ppt desde el script.
#Para ello utilizaremos los subprocesos de Python.
# Tendremos que importar el módulo subprocess:
import subprocess

#Creamos un subproceso que ejecutará el ppt (o lo que haga falta):
subproceso = subprocess.run(["../ppt"], 
	                        capture_output=True, 
	                        text=True)

#Recogemos la salida del subproceso, que será una cadena con espacios en blancos y \n:
jugadas = subproceso.stdout
print("--- Jugadas como cadena ---")
print(jugadas[0:100]) #mostramos los primeros 100 caracteres

#Vamos a convertir la cadena con las jugadas en una lista:
jugadas = jugadas.strip(' \n') #quitamos los espacios en blanco y \n del principio y el final
jugadas = list(jugadas.split('\n')) #convertimos en una lista (separando por los \n)
print("--- Jugadas como lista ---")
print(jugadas[0:10], "... y sigue")
  
