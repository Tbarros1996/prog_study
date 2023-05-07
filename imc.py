print("Bem Vindo ao Programa de Cálculo do IMC. Este programa foi desenvolvido por Thiago Barros")
print("Por Favor defina a sua ALTURA em Metros")
a = float(input(""))
if a <= 0:
    while True:    #This simulates a Do Loop
        print("Valor Negativo ou Zero; Corrija")
        a = float(input())
        if not(a <= 0): break   #Exit loop
print("Por favor defina o seu PESO em Quilogramas")
p = float(input())
if p < 0:
    while True:    #This simulates a Do Loop
        print("CORRIJA A ALTURA QUE É NEGATIVA OU NULA")
        p = float(input())
        if not(p <= 0): break   #Exit loop
iMC = p / (a * a)
print(str(iMC) + "Este é seu IMC")
if iMC < 20:
    print(" voce está MUITO MAGRO")
else:
    if iMC >= 20 and iMC <= 25:
        print("Você está NORMAL")
    else:
        if iMC >= 25 and iMC <= 30:
            print("Você está GORDO")
        else:
            if iMC >= 30 and iMC <= 40:
                print("Você está OBESO")
            else:
                print("Você está OBESO MÓRBIDO")

