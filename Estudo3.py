"""
Programação em Python
Computação para Engenharia
Thiago Barros

Problema 1 - Calculo da Duração do Ano nos Planetas do Sistema Solar

"""

""" 
Queremos que o usuário saiba quantos dias tem um ano em um planeta
então teremos que fazer com que ele entre com a a velocidade a a distância entre esse planeta e o sol
"""
from math import pi

print("Bom dia, favor colocar os valores dos dados nas unidades SI das respectivas grandezas")

velocity_planet = input(print("A velocidade do Planeta é  :"))
radius_planet = input(print("A distância do planeta pro sol é  :"))

# Agora calculando os valores do ano nos planetas

r = (float(radius_planet))
v = (float(velocity_planet)*10000)  # É importante manter as mesmas classes de valores para o python

year = 2*pi*(r/v)

year = year/(60*60*24)

  # Fazendo uma regra de 3 relacionando segundos e ano você chega nessa relação

print("O ano nesse planeta possui ", (year), "Dias")


