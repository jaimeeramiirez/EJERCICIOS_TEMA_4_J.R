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
    contador = 0
    x1 = x0 - f(x0) / df(x0)
    while abs(x1 - x0) > tol and iter_count < max_iter:
        x0 = x1
        x1 = x0 - f(x0) / df(x0)
        iter_count += 1
    return x1, iter_count




