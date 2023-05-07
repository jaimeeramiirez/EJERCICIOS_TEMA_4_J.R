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


# Encuentra un intervalo que contenga una raíz para el método de bisección
a, b = -10, 10
while np.sign(f(a)) == np.sign(f(b)):
    a -= 1
    b += 1

sol_bisection, iter_bisection = biseccion(f, a, b, tol, max_iter)
sol_secant, iter_secant = secante(f, a, b, tol, max_iter)
sol_newton_raphson, iter_newton_raphson = newton(f, df, (a + b) / 2, tol, max_iter)

print("Método\t\tCantidad de iteraciones\t       Solución")
print(f"Bisección\t{iter_bisection}\t\t\t{sol_bisection}")
print(f"Secante\t\t{iter_secant}\t\t\t{sol_secant}")
print(f"Newton-Raphson\t{iter_newton_raphson}\t\t\t{sol_newton_raphson}")

diff_sec_bis = abs(sol_secant - sol_bisection)
diff_newt_bis = abs(sol_newton_raphson - sol_bisection)
diff_newt_sec = abs(sol_newton_raphson - sol_secant)

print(f"\nDiferencia en decimales:")
print(f"Secante-Bisección: {diff_sec_bis:.6f}")
print(f"Newton-Raphson-Bisección: {diff_newt_bis:.6f}")
print(f"Newton-Raphson-Secante: {diff_newt_sec:.6f}")





