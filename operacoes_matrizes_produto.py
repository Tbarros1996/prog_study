# Operações de Produto Matricidal


# Lembre-se, uma matriz só pode ser multiplicada por outra se o numero de colunas da primeira é igual ao de linhas
# da segunda e as operações. A resposta será sempre uma matriz com o número de linhas da primeira com o
# número de colunas da segunda


# Exemplo

import numpy as np

matriz_A = np.array([[2, 3, 1], [(-1), 0, 2]])
matriz_B = np.array([[1, (-2)], [0, 5], [4, 1]])

comparacao = matriz_A == matriz_B
print(comparacao)




matriz_c = np.array([[1, 2, 3], [1, 2, 3]])
matriz_d = np.array([[1, 2, 3], [1, 2, 2]])

mc2 = matriz_c == matriz_d

print(mc2.all())
