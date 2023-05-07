# Computação Científica e Programação
# Thiago Barros
# Faça um programa que mostre na tela para três matrizes. O numero de elementos de cada matriz, as dimensões e a
# quantidade de linhas e colunas que tem na matriz, some e multiplique as matrizes, depois mostre o resultado das op
# rações com uma escalar
# Dada três matrizes faça um programa que compare cada uma delas e mostre um resultado na tela

# Importação do modulo Numpy

import numpy as np

# Definiçã das Matrizes para análise ->>>>> Foram escolhidas 3 matrizes 3X3

matriz1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriz2 = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]])
matriz3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriz1)
print(matriz2)
print(matriz3)

# Operações entre Escalares e Matrizes

# Escalar será a cinco

produto_matriz1_5 = matriz1 * 5
produto_matriz2_5 = matriz2 * 5
produto_matriz3_5 = matriz3 * 5

print("\n", produto_matriz1_5, "\n", produto_matriz2_5, "\n", produto_matriz3_5)

# Produto de Matrizes # Lembre-se Para um produto de Matriz Existir, A quantidade de Colunas da Primeira tem
# Que ser Igual a Quantidade de Linhas da Segunda e o Resultado será Uma Matriz Com a Quantidade de Linhas da Primeira
# Com a Quantidade de Colunas da Segunda. Como todas são 3x3 não se terá problemas
# A ordem das matrizes fará diferença no produto sim

produto_matriz1_matriz2 = matriz1 @ matriz2
produto_matriz1_matriz3 = matriz1 @ matriz3
produto_matriz2_matriz3 = matriz2 @ matriz3

print(produto_matriz1_matriz2, produto_matriz1_matriz3, produto_matriz2_matriz3)

# Vamos trabalhar com matrizes e condicionais e o modulo if ----> Usando a Função all()

comparacao_matriz1_matriz2 = matriz1 == matriz2
print(comparacao_matriz1_matriz2)
comparacao_1 = comparacao_matriz1_matriz2.all()
print(comparacao_1)

if comparacao_1 == bool(0 == 0):
    print("As matrizes são Iguais")
else:
    print("As matrizes são Diferentes")

comparacao_matriz1_matriz3 = matriz1 == matriz3
print(comparacao_matriz1_matriz3)
comparacao_2 = comparacao_matriz1_matriz3.all()
print(comparacao_2)

if comparacao_2 == bool(0 == 0):
    print("As matrizes são Iguais")
else:
    print("As matrizes são Diferentes")

comparacao_matriz2_matriz3 = matriz2 == matriz3
print(comparacao_matriz2_matriz3)
comparacao_3 = comparacao_matriz2_matriz3.all()
print(comparacao_3)

if comparacao_3 == bool(0 == 0):
    print("As matrizes são Iguais")
else:
    print("As matrizes são Diferentes")

# Usando a Comparação de Funções com a função np.array_equal()


comparacao_4 = np.array_equal(matriz1, matriz2)

if comparacao_4 == bool(0 == 0):
    print("As matrizes são Iguais")
else:
    print("As matrizes são Diferentes")

comparacao_5 = np.array_equal(matriz1, matriz3)

if comparacao_5 == bool(0 == 0):
    print("As matrizes são Iguais")
else:
    print("As matrizes são Diferentes")

comparacao_6 = np.array_equal(matriz2, matriz3)

if comparacao_6 == bool(0 == 0):
    print("As matrizes são Iguais")
else:
    print("As matrizes são Diferentes")
