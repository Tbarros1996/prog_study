# Lista de Exercício 4

# Programa que calcula a média e verifica se o aluno está passado ou reprovado

nota_1 = input(print("Entre com a primeira nota do aluno: "))
nota_2 = input(print("Entre com a segunda nota do aluno:  "))
nota_3 = input(print("Entre com a terceira nota do aluno: "))
nota_4 = input(print("Entre com a quarta nota do aluno:   "))

media_aluno = (float(nota_1) + float(nota_2) + float(nota_3) + float(nota_4)) / 4

print("A media do Aluno foi de: \n ", media_aluno)

if media_aluno >= 7.0:
    print("Aluno está Aprovado")
elif media_aluno < 7:
    print("Aluno Está Reprovado")
