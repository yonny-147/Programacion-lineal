import numpy as np
import matplotlib.pyplot as plt

def agregar_desigualdad():
    """
    Solicita al usuario que ingrese una desigualdad en el formato 'ax + by <= c' o 'ax + by >= c'.
    
    La función analiza la entrada, extrae los coeficientes de x y y, el signo de la desigualdad y el valor constante.
    Maneja casos en los que los coeficientes son implícitos (por ejemplo, si x no tiene coeficiente visible, se asume como 1).
    
    Retorna:
        - a (float): Coeficiente de la variable x.
        - b (float): Coeficiente de la variable y.
        - signo (str): Signo de la desigualdad ('<=' o '>=').
        - c (float): El término constante de la desigualdad.
        
    Si la entrada es incorrecta, imprime un mensaje de error y retorna None.
    """
    desigualdad = input("Ingresa una desigualdad (ejemplo: 2x + 3y <= 6 o x - y >= 4): ").strip()

    # Intentar dividir la entrada en sus componentes (coeficientes, signo y constante)
    try:
        partes = desigualdad.split()

        # Verificar que haya exactamente 5 partes y que el signo sea <= o >=
        if len(partes) != 5 or (partes[3] != "<=" and partes[3] != ">="):
            raise ValueError("Formato incorrecto")

        # Extraer y procesar los coeficientes de 'x' y 'y' (manejar casos implícitos como 'x' o '-y')
        a = partes[0].replace('x', '')
        b = partes[2].replace('y', '')

        # Convertir los coeficientes en floats, manejando valores implícitos (ejemplo: 'x' se convierte en 1)
        a = 1.0 if a == '' or a == '+' else (-1.0 if a == '-' else float(a))
        b = 1.0 if b == '' or b == '+' else (-1.0 if b == '-' else float(b))

        # Capturar el signo y la constante
        signo = partes[3]  # El signo puede ser '<=' o '>='
        c = float(partes[4])  # El valor constante al otro lado de la desigualdad

        return a, b, signo, c
    except ValueError:
        # Si hay un error en el formato, se notifica al usuario y retorna None
        print("\nError: Formato incorrecto. Asegúrate de ingresar la desigualdad como 'ax + by <= c' o 'ax + by >= c'.\n")
        return None

def plot_desigualdades(desigualdades):
    """
    Grafica las desigualdades ingresadas por el usuario y muestra la región factible donde se cumplen todas.
    
    Parámetros:
        - desigualdades (list): Lista de tuplas, donde cada tupla representa una desigualdad en la forma (a, b, signo, c).
          'a' y 'b' son los coeficientes de x e y, 'signo' es la relación de desigualdad ('<=' o '>='), y 'c' es la constante.
    """
    x = np.linspace(-10, 10, 400)  # Genera valores de x en el rango [-10, 10]

    # Crear una figura y definir los límites del gráfico
    fig, ax = plt.subplots()
    ax.set_xlim(-10, 10)  # Límite en el eje X
    ax.set_ylim(-10, 10)  # Límite en el eje Y
    
    # Iterar sobre cada desigualdad y graficarla
    for a, b, signo, c in desigualdades:
        if b != 0:
            # Despejar y de la ecuación: ax + by <= c => y = (c - a * x) / b
            y = (c - a * x) / b
        else:
            # Caso especial cuando b es 0 (la ecuación es de la forma ax <= c)
            y = np.full_like(x, c / a)  # Todos los valores de y serán constantes

        # Graficar y sombrear la región factible según el signo de la desigualdad
        if signo == "<=":
            ax.fill_between(x, y, -10, where=(y >= -10), interpolate=True, alpha=0.3, label=f"{a}x + {b}y <= {c}")
        elif signo == ">=":
            ax.fill_between(x, y, 10, where=(y <= 10), interpolate=True, alpha=0.3, label=f"{a}x + {b}y >= {c}")
    
    # Agregar ejes X e Y en el gráfico
    plt
