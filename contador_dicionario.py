
"""
Algoritmo do livro pense python

A primeira linha da função cria um dicionário vazio. O loop for atravessa a string. Cada vez que passa pelo loop,
se o caractere c não estiver no dicionário, criamos um item com a chave c e o
valor inicial 1 (pois já vimos esta letra uma vez). Se o c já estiver no dicionário, incrementamos d [c].
"""

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
            print(d)
        else:
            d[c] += 1
            print(d)
    return d

x = input(print("Entre com a Palavra"))
histogram(x)
