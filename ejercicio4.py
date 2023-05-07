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
