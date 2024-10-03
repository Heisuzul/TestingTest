import math

# Definimos la función f(x) = tan(x) - x
def f(x):
    return math.tan(x) - x

# Definimos la derivada f'(x) = sec^2(x) - 1
def f_deriv(x):
    return 1 / math.cos(x)**2 - 1

# Método de Newton
def metodo_newton(f_prima, x0, steps=10):
    # Mostrar el valor inicial X0

    for i in range(steps):
        f_evaluada = f(x0)
        f_prima_evaluada = f_prima(x0)
        x1 = x0 - f_evaluada / f_prima_evaluada
        # Actualizamos x0 para el siguiente paso
        x0 = x1
    return x1

# Llamada al método de Newton
x0 = 4.5
x1 = 7.7
solucion0 = metodo_newton(f_deriv, x0)
solucion1 = metodo_newton(f_deriv, x1)


print("Solución aproximada de 4.5:", solucion0)
print("Solución aproximada de 7.7:", solucion1)
