# Vamos aplicar uma análise de lógica para matrizes

import numpy as np
import math as mt

primeira_matriz = np.array([[1, 2, 3], [4, 5, 6]])
segunda_matriz = np.array([[2, 3, 3], [4, 4, 6]])

x = primeira_matriz==segunda_matriz
print(x)


#Comparando a matriz usando a função all()

primeira_matriz = np.array([[1,2,3],[3,2,1]])
segunda_matriz = np.array([[32,45,99],[7,3,8]])
matriz_comparacao = primeira_matriz==segunda_matriz
resultado_comparacao = matriz_comparacao.all()
print(resultado_comparacao)