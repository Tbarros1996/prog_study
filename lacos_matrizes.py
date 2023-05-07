# Faça um laço de forma que todos os elementos e uma das matrizes sejam iguais aos elementos da
# Matriz de referencia


import numpy as np

matriz1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriz2 = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]])
matriz3 = np.array([[10000, 20000, 30000], [40000, 50000, 60000], [70000, 80000, 90000]])  # Matriz de Reference

# Comparação Elemento a Elemento

if np.array_equal(matriz1, matriz3) == bool(0 == 0):
    print("As matrizes são Iguais")
else:
    print("As matrizes são diferentes")
    print("Iniciando Processo de Calculo")

interacao = 0
while np.array_equal(matriz1, matriz3) == bool(0 != 0):
    interacao = interacao
    matriz_pra_interar = matriz1
    matriz_objetivo = matriz3
    print("A matriz para ser Interada é: ")
    print(matriz_pra_interar)
    print("A matriz que se tem como Objetivo é: ")
    print(matriz_objetivo)
    matriz_pra_interar = matriz_pra_interar * interacao

    """
    A matriz de interar é um lixo de memória para servir de referencia para sabermos quantas interações
    estamos faltando para igualarmos as matrizes
    
    """
    print(matriz_pra_interar, "Interação:", interacao)
    interacao = interacao + 1

    if interacao > 1000000000:
        print("Matrizes Impossiveis de Calcular")
        break

    if np.array_equal(matriz_pra_interar, matriz_objetivo) == bool(0 == 0):
        print("As Matrizes são Iguais")
        print("Ocorreram :", interacao, "Interações para a Obteção da Igualdade")
        break