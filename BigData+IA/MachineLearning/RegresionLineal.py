# numpy (np): Para cálculo numérico eficiente (medias, sumas, operaciones vectorizadas).
#matplotlib.pyplot (plt): Para graficar los datos y la recta ajustada.

import numpy as np
import matplotlib.pyplot as plt

# En este ejemplo básico, cargamos los datos manualmente en arrays de numpy
inversion = np.array([16000, 32000, 48000, 56000, 64000, 80000], dtype=float)
ventas = np.array([10000000, 15000000, 20000000, 22000000, 30000000, 32000000], dtype=float)

# Calculamos los coeficientes de correlación y de determinación para ver el grado de acierto de nuestra regresión lineal.
# En este caso, NO aplicamos la fórmula, sino que usamos la función corrcoef de la librería numpy.

r = np.corrcoef(inversion, ventas)[0, 1]
r2 = r**2

# Mostramos la fórmula de la recta obtenida, particularizando para inversión y ventas.
print("=== REGRESIÓN LINEAL ===")
print(f"Ecuación de regresión: Ventas = {a:.2f} + {b:.2f} * Inversión")

# Mostramos el coeficiente de correlación obtenido y una valoración de su resultado.
print(f"Coeficiente de determinación (r2): {r2:.4f}")
if abs(r2) > 0.9:
    print("Existe una relación lineal muy fuerte entre inversión y ventas.")
elif abs(r2) > 0.7:
    print("Existe una relación lineal fuerte entre inversión y ventas.")
elif abs(r2) > 0.4:
    print("Existe una relación lineal moderada entre inversión y ventas.")
elif abs(r2) > 0.1:
    print("Existe una relación lineal débil entre inversión y ventas.")
else:
    print("La relación lineal es prácticamente nula.")

# Mostramos la predicción de ventas para una inversión en publicidad de 95.000€, tal y como pide el enunciado del ejercicio
x_pred = 95000
y_pred = a + b * x_pred
print(f"Predicción de ventas para una inversión de {x_pred:,.0f} €: {y_pred:,.0f} €")

plt.scatter(inversion, ventas, color='blue', label='Datos reales')
plt.plot(inversion, a + b * inversion, color='red', label='Recta de regresión')
plt.title('Relación entre inversión en publicidad y ventas')
plt.xlabel('Inversión en publicidad (€)')
plt.ylabel('Ventas (€)')
plt.legend()
plt.grid(True)
plt.show()
