import numpy as np
import timeit

def coef_recursivo(f, t, T, n):
    if n == 0:
        return (2 / T) * np.trapz(f, t), np.zeros(0), np.zeros(0)
    
    a_n = (2 / T) * np.trapz(f * np.cos(2 * np.pi * n * t / T), t)
    b_n = (2 / T) * np.trapz(f * np.sin(2 * np.pi * n * t / T), t)
    
    a0, an, bn = coef_recursivo(f, t, T, n - 1)
    return a0, np.append(an, a_n), np.append(bn, b_n)

def fourier_recursivo(f, t, T, N):
    return coef_recursivo(f, t, T, N)

T = 2 * np.pi
t = np.linspace(0, T, 1000, endpoint=False)
f = np.sign(np.sin(t))

inicio = timeit.default_timer()
a0, an, bn = fourier_recursivo(f, t, T, 10)
fin = timeit.default_timer()
tiempo_recursivo = fin - inicio

print(f"Coeficiente a0: {a0:.6f}")
print(f"Coeficientes an: {an}")
print(f"Coeficientes bn: {bn}")
print(f"Tiempo recursivo: {tiempo_recursivo:.6f} segundos")
