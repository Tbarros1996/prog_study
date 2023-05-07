"""
Thiago Barros

Software de Calculo de Idade e dias de Vida

"""

print("Olá, como vai você?;), Bom primeiramente pode dizer seu nome:? ")

nome = str(input(print("Escreva seu nome")))

print("Bom,", nome, ", Seja bem vindo \n \n \n ")

print("Ok, agora vamos calcular sua idade;)")

print("Precisamos de algumas informações....")

dia = int(input(print("Qual dia você nasceu???\n")))

if dia <= 0 or dia > 31:
    while dia <= 0 or dia > 31:
        dia = int(input(print("Dia impossivel, por favor corrija. \n Qual dia você nasceu???\n")))

mes = int(input(print("Qual mês nasceu???, entre com o número, por exemplo: Janeiro = 1 \n")))
if mes <= 0 or mes > 12:
    while mes <= 0 or mes > 12:
        dia = int(input(print("Mes impossivel, por favor corrija. \n Qual mes você nasceu???\n")))

ano = input(print("Qual ano você nasceu???\n"))

data_de_nascimento = [dia, mes, ano]

if mes == 1:
    mes_extenso = "Janeiro"

if mes == 2:
    mes_extenso = "Fevereiro"

if mes == 3:
    mes_extenso = "Março"

if mes == 4:
    mes_extenso = "Abril"

if mes == 5:
    mes_extenso = "Maio"

if mes == 6:
    mes_extenso = "Junho"

if mes == 7:
    mes_extenso = "Julho"

if mes == 8:
    mes_extenso = "Agosto"

if mes == 9:
    mes_extenso = "Setebro"

if mes == 10:
    mes_extenso = "Outubro"

if mes == 11:
    mes_extenso = "Novembro"

if mes == 12:
    mes_extenso = "Dezembro"

print("Sua data de nascimento é:", dia, "de", mes_extenso, "de", ano)

print("Agora Escreva o dia de Hoje, o mês e o ano:")

dia_hoje = int(input(print("Qual dia de hoje ??\n")))

if dia_hoje <= 0 or dia_hoje > 31:
    while dia_hoje <= 0 or dia_hoje > 31:
        dia = int(input(print("Dia impossivel, por favor corrija. \n Qual dia atual???\n")))

mes_hoje = int(input(print("Qual mês nos estamos???\n")))

if mes_hoje <= 0 or mes_hoje > 12:
    while mes_hoje <= 0 or mes_hoje > 12:
        dia = int(input(print("Mes impossivel, por favor corrija. \n Qual mes atual???\n")))

ano_hoje = int(input(print("Qual ano atual\n ")))

dia_zero = dia

mes_zero = mes

ano_zero = ano

data_inicial = [int(dia_zero), int(mes_zero), int(ano_zero)]
data_final = [int(dia_hoje), int(mes_hoje), int(ano_hoje)]

# Para os dias

d = 0
m = 0
a = 0

# Desconsiderando que existe anos bissextos e considerando que todos os meses tem 30 dias


while data_inicial[2] < data_final[2]:
    data_inicial[0] = data_inicial[0] + 1
    d = d + 1
    print("Hoje é", d, "de", m, "de", a)
    if data_inicial[0] > 30:
        data_inicial[0] = 1
        d = 0
        data_inicial[1] = data_inicial[1] + 1
        m = m + 1
    if data_inicial[1] > 12:
        data_inicial[0] = 1
        d = 0
        data_inicial[1] = 1
        m = 0
        data_inicial[2] = data_inicial[2] + 1
        a = a + 1
    if (data_inicial[2] == data_final[2]) and (data_inicial[0] == data_final[0]) and (data_inicial[1] == data_final[1]):
        break

print("Você nasceu a ", d + m * 30 + a * 12 * 30, "dias \n \n \n")
print("Voce tem: ", a, "anos")

print("É IMPORTANTE SALIETAR QUE ESSE PROGRAMA NÃO CONSIDERA ANOS BISSEXTOS E TODOS OS MESES TEM MESMA QUANTIDADE"
      "DE DIAS:30")
