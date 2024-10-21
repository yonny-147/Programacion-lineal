import random
import matplotlib.pyplot as plt
import numpy as np

# Generamos la ecuación lineal aleatoria: y = mx + b
m = random.uniform(-10, 10)  # Pendiente aleatoria entre -10 y 10
b = random.uniform(-10, 10)  # Intersección aleatoria entre -10 y 10

print("Adivina los parámetros de la ecuación lineal de la forma y = mx + b")

# Creamos un gráfico de la ecuación para que el jugador vea algunos puntos
x_vals = np.linspace(-10, 10, 100)
y_vals = m * x_vals + b

# Mostramos los puntos
plt.plot(x_vals, y_vals, label="Recta")
plt.scatter(x_vals, y_vals, color="red", s=10, label="Puntos")
plt.title("Visualización de la ecuación lineal: y = mx + b")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

# Iniciamos el juego
intentos = 3

while intentos > 0:
    # Pedimos al usuario que adivine la pendiente y la intersección
    m_guess = float(input("Adivina la pendiente (m): "))
    b_guess = float(input("Adivina la intersección con el eje y (b): "))

    # Comprobamos si la adivinanza es correcta
    if abs(m_guess - m) < 0.1 and abs(b_guess - b) < 0.1:        print("¡Correcto! La ecuación es y = {:.2f}x + {:.2f}".format(m, b))
        break
    else:
        intentos -= 1
        print("Incorrecto. Te quedan {} intentos.".format(intentos))
        if intentos > 0:
            print("¡Intenta de nuevo!")

if intentos == 0:
    print("Has fallado. La respuesta correcta es y = {:.2f}x + {:.2f}".format(m, b))
