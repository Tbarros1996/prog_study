y = int(input(print("Valor Inicial:  ")))
for x in range(y): #Lembre-se Que com base no Documento do Python, O valor inicial, quando não definido, o valor
    # do espaçamento é sempre range
    x = y-x
    print(x)
    if x == 1:
        print("Cabum")
