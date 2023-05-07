import numpy as np

def f(x):
    return x**3 + x + 16

#Función de bisección
def biseccion(f, a, b, tol, max_iter):
    contador = 0
    while (b - a) / 2 > tol and contador < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        contador += 1
    return c, contador

#Función secante
def secante(f, x0, x1, tol, max_iter):
    contador = 0
    while abs(x1 - x0) > tol and contador < max_iter:
        x_new = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0, x1 = x1, x_new
        contador += 1
    return x1, contador

#Función de Newton

def df(x): #Derivada de la función para el método de Newton
    return 3 * x**2 + 1

def newton(f, f_derivada, x0, tol, max_iter):
    f_derivada = np.vectorize(f_derivada)
    contador = 0
    x1 = x0 - f(x0) / df(x0)
    while abs(x1 - x0) > tol and contador < max_iter:
        x0 = x1
        x1 = x0 - f(x0) / df(x0)
        contador += 1
    return x1, contador

tol = 1e-6
max_iter = 100


# Esta parte del código utiliza un bucle while para encontrar dos valores a y b en el intervalo [-10, 10]
# que tengan signos opuestos de la función f.
# Esto se hace porque el método de bisección
# solo funciona si hay un cambio de signo en la función dentro del intervalo.
# Si no hay un cambio de signo, el método de bisección no funcionará.

def comparar_metodos(f, df, a, b, tol, max_iter):
    # Encontrar intervalo que contenga una raíz para el método de bisección
    while np.sign(f(a)) == np.sign(f(b)):
        a -= 1
        b += 1

    # Aplicar los métodos de bisección, secante y Newton-Raphson
    sol_biseccion, iter_biseccion = biseccion(f, a, b, tol, max_iter)
    sol_secante, iter_secante = secante(f, a, b, tol, max_iter)
    sol_newton, iter_newton = newton(f, df, (a+b)/2, tol, max_iter)

    # Imprimir resultados de los métodos
    print("Método\t\tCantidad de iteraciones\tSolución")
    print(f"Bisección\t{iter_biseccion}\t\t\t{sol_biseccion}")
    print(f"Secante\t\t{iter_secante}\t\t\t{sol_secante}")
    print(f"Newton\t\t{iter_newton}\t\t\t{sol_newton}")

    # Calcular las diferencias de decimales entre los métodos
    print(f"Diferencia de decimales entre bisección y secante: {abs(sol_biseccion - sol_secante)}") 
    print(f"Diferencia de decimales entre bisección y Newton: {abs(sol_biseccion - sol_newton)}")
    print(f"Diferencia de decimales entre secante y Newton: {abs(sol_secante - sol_newton)}")

if __name__ == "__main__":
    comparar_metodos(f, df, a, b, tol, max_iter)