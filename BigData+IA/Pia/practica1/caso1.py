#La idea es ejecutar ppt y redirigir su salida a este script de python.
#En el script de python la entrada se lee con input().

#El esquema general será algo similar a:
# ppp | python fichero.py

lista = []
for i in range(0, 100):
	entrada = input()
	lista.append(entrada)

print("Esta en la entrada que hemos recogido")
print(lista[0:10], "... y sigue.")