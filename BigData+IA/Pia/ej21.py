# Lista vacía para guardar los nombres de los invitados
todosInvitados = list()

# Variable para controlar la entrada de nombres
nombre = ""

# Repetimos hasta que se escriba "fin"
while nombre != "fin":
    print('Nombre ("fin" para terminar):')
    nombre = str(input())
    if nombre != "fin":
        todosInvitados.append(nombre)

# Solicitamos el número de plazas disponibles
print("Nº de plazas de la fiesta:")
numPlazas = int(input())

# Ordenamos la lista completa antes de separar asistentes y lista de espera
todosInvitados.sort()  # Ordena la lista alfabéticamente (A-Z)

# Separamos los asistentes y los que quedan en lista de espera
asistentes = todosInvitados[0:numPlazas]
listaEspera = todosInvitados[numPlazas:]

# Mostramos los resultados
print("Asistentes (ordenados):", asistentes)
print("Lista de espera (ordenada):", listaEspera)
