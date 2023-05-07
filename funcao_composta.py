# Programa que calcula o Valor de Uma Função e O resultado com base na entrada de Dois Valores Numéricos

"""

            x+y para x>=0 e y>=0
f(x,y) =    x+y**2 para x>=0 e y<0
            x**2 + y para x<0 e y>=0
            x**2 + y**2 para x<0 e y<0

"""


def f(x, y):  # Primeiro Metodo de Resolução do Problema
    x = float(x)
    y = float(y)
    if x >= 0 and y >= 0:
        print("X e Y são Maiores ou Iguais a Zero, Logo: ")
        resultado = x + y
        print(resultado)
    elif x >= 0 and y < 0:
        print('X é maior Ou Igual a Zero E Y é Negativo')
        resultado = x + y ** 2
        print(resultado)
    elif x < 0 and y >= 0:
        print("X é Negativo e Y é maior ou Igual a Zero")
        resultado = x ** 2 + y
        print(resultado)
    else:
        print("Ambos são Negativos")
        resultado = x ** 2 + y ** 2
        print(resultado)


x = float(input(print("Entre com O Valor de X")))
y = float(input(print("Entre com O Valor de Y")))

f(x, y)
