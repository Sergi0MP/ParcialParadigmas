import numpy as np
import timeit

def fourier_iterativo(f, t, T, N):
    a0 = (2 / T) * np.trapz(f, t)
    an = np.zeros(N)
    bn = np.zeros(N)

    for n in range(1, N + 1):
        an[n - 1] = (2 / T) * np.trapz(f * np.cos(2 * np.pi * n * t / T), t)
        bn[n - 1] = (2 / T) * np.trapz(f * np.sin(2 * np.pi * n * t / T), t)

    return a0, an, bn

T = 2 * np.pi
t = np.linspace(0, T, 1000, endpoint=False)
f = np.sign(np.sin(t))

inicio = timeit.default_timer()
a0, an, bn = fourier_iterativo(f, t, T, 10)
fin = timeit.default_timer()
tiempo_iterativo = fin - inicio

print(f"Coeficiente a0: {a0:.6f}")
print(f"Coeficientes an: {an}")
print(f"Coeficientes bn: {bn}")
print(f"Tiempo iterativo: {tiempo_iterativo:.6f} segundos")
