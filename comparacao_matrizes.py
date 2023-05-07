# Comparação de Matrizes com a função np.array_equal()

import numpy as np

matriz_A = np.array([[2, 3, 1], [(-1), 0, 2]])
matriz_B = np.array([[1, (-2)], [0, 5], [4, 1]])
matriz_c = np.array([[1, 2, 3], [1, 2, 3]])
matriz_d = np.array([[1, 2, 3], [1, 2, 3]])
primeira_matriz = np.array([[1, 2, 3], [3, 2, 1]])
segunda_matriz = np.array([[32, 45, 99], [7, 3, 8]])
primeira_matriz2 = np.array([[1, 2, 3], [4, 5, 6]])
segunda_matriz2 = np.array([[2, 3, 3], [4, 4, 6]])

#Comparação 1

print(np.array_equal(matriz_A,matriz_A))#Matriz igual A Ela Mesma
print(np.array_equal(matriz_A,matriz_B))
print(np.array_equal(matriz_A,matriz_c))
print(np.array_equal(matriz_c,matriz_A))
print(np.array_equal(matriz_c,matriz_d))
print(np.array_equal(primeira_matriz,primeira_matriz2))
