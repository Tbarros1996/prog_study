# Retorna a parte inteira, fracionaria e real e arredondado

x = float(input(print("Entre com o Número Real")))
x_fracionario = x - int(x)
print(round(x_fracionario, ndigits=6))
x_inteiro = int(abs(x))
print(x_inteiro)
x_arredondado = round(x)
print(x_arredondado)
