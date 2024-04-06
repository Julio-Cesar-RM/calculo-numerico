import numpy as np
import matplotlib.pyplot as plt

# Definindo a função
def f_function(x, y):
    return 4*x**2 + 9*y**2 - 81

# Criando valores para x e y
x = np.linspace(-6, 6, 400)
y = np.linspace(-3, 3, 300)
X, Y = np.meshgrid(x, y)

# Calculando os valores de f
F = f_function(X, Y)

# Plotando o mapa de contorno
plt.figure(figsize=(8, 6))
contour = plt.contour(X, Y, F, levels=[0], colors='r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Curva de Nível de f(x, y) = 4x^2 + 9y^2 - 81')
plt.grid(True)
plt.show()