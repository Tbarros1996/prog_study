#Comparação entre uma contagem entre while e função recursiva
x = 10

while x > 0:
    print(x)
    x = x - 1
    if x == 0:
        print("Cabum")
        break
