#3. Você pode usar um sinal de menos para fazer um número negativo como -2. O que acontece se puser
#um sinal de mais antes de um número? E se escrever assim: 2++2?
x = 2++++++2
#No caso da adição, ele somou normalmente
y = +4-5
print(x)
print(y)
#No caso da subtração ele respeitou a ordem de procedencia e calculou os resultados negativos e positivos
#4. Na notação matemática, zeros à esquerda são aceitáveis, como em 02. O que acontece se você tentar
#usar isso no Python?
#z = 02
#print(z)
# Erro de sintaxe
z1 = 2.1
print(z1)
# Formato Correto
z2 = 2,1
# Matriz Linha
print(z2)
z3 = (21)
# Erro
print(z3)

corno = 2

manso = 3

chifre = corno  manso
# Erro de sintaxe - Operador Inexistente

print(chifre)