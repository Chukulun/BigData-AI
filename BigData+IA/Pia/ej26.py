print("Nombre:")
#nombre = str(input())
nombre = "Pepito Perez"
nombre = nombre.lower() #trabajamos con los números en minúsculas
nombre = nombre.replace(' ', '')
numSuerte = set()

#ord(c) devuelve el codepoint Unicode que representa al caracter

for letra in nombre:
	numSuerte.add(ord(letra)-ord('a')+1) #se añade a un set para que no haya repeticiones y a ord le restamos el valor de a +1 para empezar en la posicion a unicode

print(numSuerte)