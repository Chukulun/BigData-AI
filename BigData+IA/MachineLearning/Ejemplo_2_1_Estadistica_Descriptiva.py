# LIBRERÍAS EMPLEADAS EN EL EJEMPLO
# Tratamiento de datos
# ==============================================================================
# Importamos la librería numpy para poder generar datos aleatorios
# de una distribución normal de media y desviacióón estándar dada
# y para calcular estadísticos descriptivos básicos
import numpy as np
import pandas as pd
# Gráficos
# ==============================================================================
import matplotlib.pyplot as plt
# Generación de datos
# ==============================================================================
muA, sigmaA = 1000, 1 # media y desviación estándar embotelladora A
muB, sigmaB = 1000, 4 # media y desviación estándar embotelladora B
datosA = np.random.normal(muA, sigmaA, 1000)
datosB = np.random.normal(muB, sigmaB, 1000)
datos=np.column_stack((datosA, datosB))
datos

np.mean(datos,axis=0) # Calcula la media aritmetica de los datos,
                      # (por columnas)

# Desviación estándar (por columnas, axis=0)
np.std(datos,axis=0)

Data = pd.DataFrame(datos, columns=['Embotelladora_A', 'Embotelladora_B'])
Data.describe()

plt.hist(datos, 50)
plt.ylabel('Número de datos')
plt.xlabel('valores')
plt.title('Histograma')
plt.show()

