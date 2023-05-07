"""
Algoritimo Conversor de Temperatura

tb1996

Nesse algoritmo se trabalha comparação e string

"""
temperatura = input(print("Qual o valor da temperatura que você deseja converter? \n "))

unidade = input(str((print("Qual o valor da unidade dessa temperatura? \n [COLOQUE F PARA FAHRENHEIT, K PARA KELVIN "
                           "OU C PARA CELCIUS]  \n "))))

saida_temperatura = input(str((print("Qual o valor da unidade para ser convertida \n "
                                     "[COLOQUE F PARA FAHRENHEIT, K PARA KELVIN OU C PARA CELCIUS]  \n "))))

temperatura = float(temperatura)

if unidade in ["K", "k"]:
    unidade_entrada = "Kelvin"
if unidade in ["C", "c"]:
    unidade_entrada = "Celcius"
if unidade in ["F", "f"]:
    unidade_entrada = "Fahrenheit"

if saida_temperatura in ["K", "k"]:
    unidade_saida = "Kelvin"
if saida_temperatura in ["C", "c"]:
    unidade_saida = "Celcius"
if saida_temperatura in ["F", "f"]:
    unidade_saida = "Fahrenheit"

if unidade in ["K", "k"] and saida_temperatura in ["C", "c"]:  #
    conversao1 = temperatura + 270
    print("Você pediu para converter: ", temperatura, "Da qual a Unidade é: "
      , unidade_entrada, "Para:  ", unidade_saida, "E o valor é  :",conversao1)

elif unidade in ["C", "c"] and saida_temperatura in ["K", "k"]:
    conversao2 = temperatura - 272
    print("Você pediu para converter: ", temperatura, "Da qual a Unidade é: "
          , unidade_entrada, "Para:  ", unidade_saida, "E o valor é  :", conversao2)

if unidade in ["C", "c"] and saida_temperatura in ["F", "f"]:
    conversao3 = (temperatura*1.8) +32
    print("Você pediu para converter: ", temperatura, "Da qual a Unidade é: "
          , unidade_entrada, "Para:  ", unidade_saida, "E o valor é  :", conversao3)

elif unidade in ["F", "f"] and saida_temperatura in ["C", "c"]:
    conversao4 = (temperatura-32)/1.8
    print("Você pediu para converter: ", temperatura, "Da qual a Unidade é: "
          , unidade_entrada, "Para:  ", unidade_saida, "E o valor é  :", conversao4)

if unidade in ["K", "k"] and saida_temperatura in ["F", "f"]:
    conversao5 = (temperatura - 273) * 1, 8 + 32
    print("Você pediu para converter: ", temperatura, "Da qual a Unidade é: "
          , unidade_entrada, "Para:  ", unidade_saida, "E o valor é  :", conversao5)

elif unidade in ["F", "f"] and saida_temperatura in ["K", "k"]:
    conversao6 = (temperatura - 32) * (5 / 9) + 273
    print("Você pediu para converter: ", temperatura, "Da qual a Unidade é: "
          , unidade_entrada, "Para:  ", unidade_saida, "E o valor é  :", conversao6)

