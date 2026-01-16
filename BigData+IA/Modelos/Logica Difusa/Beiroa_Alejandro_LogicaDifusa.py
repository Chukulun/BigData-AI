import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Rangos de valores que pueden tomar las variables difusas
temperatura = ctrl.Antecedent(np.arange(-10, 41, 1), 'temperatura')
humedad = ctrl.Antecedent(np.arange(0, 101, 1), 'humedad')
potencia = ctrl.Consequent(np.arange(0, 101, 1), 'potencia')

# Indicamos que genere 3 funciones de pertenencia automáticamente para cada
# antecedente con las etiquetas lingüísticas indicadas
temperatura.automf(names=['baja', 'media', 'alta'])
humedad.automf(names=['baja', 'media', 'alta'])

# Definimos manualmente las funciones de pertenencia utilizando conjuntos
# triangulares para el consecuente; los puntos del triángulo se introducen en
# sentido horario comenzando por el extremo izquierdo
potencia['muy_baja'] = fuzz.trimf(potencia.universe, [0, 0, 33])
potencia['baja'] = fuzz.trimf(potencia.universe, [0, 33, 67])
potencia['alta'] = fuzz.trimf(potencia.universe, [33, 67, 100])
potencia['muy_alta'] = fuzz.trimf(potencia.universe, [67, 100, 100])

# Visualizar las funciones de pertenencia
temperatura.view()
plt.title('Funciones de pertenencia - Temperatura (°C)')

humedad.view()
plt.title('Funciones de pertenencia - Humedad (%)')

potencia.view()
plt.title('Funciones de pertenencia - Potencia (%)')

plt.show(block=True)

# Definimos las reglas y las asociamos con el sistema
sistema_calefaccion = ctrl.ControlSystemSimulation(ctrl.ControlSystem([
    ctrl.Rule(temperatura['alta'] & (humedad['alta'] | humedad['media']), potencia['muy_baja']),
    ctrl.Rule(temperatura['media'], potencia['baja']),
    ctrl.Rule(temperatura['baja'], potencia['alta']),
    ctrl.Rule(temperatura['baja'] & humedad['alta'], potencia['muy_alta'])
]))

# EJEMPLO 1: Día caluroso y húmedo (verano)
print("\n" + "="*60)
print("EJEMPLO 1: Día caluroso y húmedo")
print("="*60)
sistema_calefaccion.input['temperatura'] = 35
sistema_calefaccion.input['humedad'] = 80
sistema_calefaccion.compute()
print(f"Temperatura: 35°C")
print(f"Humedad: 80%")
print(f"Potencia de calefacción: {sistema_calefaccion.output['potencia']:.2f}%")

potencia.view(sim=sistema_calefaccion)
plt.title("Ejemplo 1: Día caluroso y húmedo (35°C, 80%)")


# EJEMPLO 2: Día frío con poca humedad (regla 3: solo alta)
print("\n" + "="*60)
print("EJEMPLO 2: Día frío con humedad baja")
print("="*60)
sistema_calefaccion.input['temperatura'] = 0
sistema_calefaccion.input['humedad'] = 20
sistema_calefaccion.compute()
print(f"Temperatura: 0°C")
print(f"Humedad: 20%")
print(f"Potencia de calefacción: {sistema_calefaccion.output['potencia']:.2f}%")
print("(Regla 3 activa: temperatura baja → potencia alta)")

potencia.view(sim=sistema_calefaccion)
plt.title("Ejemplo 2: Día frío y seco (0°C, 20%)")


# EJEMPLO 3: Día frío y húmedo (regla 4 tiene prioridad sobre regla 3)
print("\n" + "="*60)
print("EJEMPLO 3: Día frío y muy húmedo")
print("="*60)
sistema_calefaccion.input['temperatura'] = 0
sistema_calefaccion.input['humedad'] = 85
sistema_calefaccion.compute()
print(f"Temperatura: 0°C")
print(f"Humedad: 85%")
print(f"Potencia de calefacción: {sistema_calefaccion.output['potencia']:.2f}%")
print("(Regla 4 activa: temperatura baja Y humedad alta → potencia MUY ALTA)")
print("(La regla 4 tiene PRIORIDAD sobre la regla 3)")

potencia.view(sim=sistema_calefaccion)
plt.title("Ejemplo 3: Día frío y húmedo (0°C, 85%)")

plt.show(block=True)