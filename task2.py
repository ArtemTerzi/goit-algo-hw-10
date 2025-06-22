import numpy as np
import scipy.integrate as spi

a = 0
b = np.pi
N = 100000 

def f(x):
    return x*np.cos(x)

x_rand = np.random.uniform(a, b, N)
y_rand = f(x_rand)
integral_mc = (b - a) * np.mean(y_rand)

print("Інтеграл методом Монте-Карло:", integral_mc)

result, error = spi.quad(f, a, b)
print("Інтеграл методом quad:", result)
print("Абсолютна похибка:", abs(integral_mc - result))