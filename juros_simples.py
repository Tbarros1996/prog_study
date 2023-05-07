# Função para calcular taxa de Juros Simples

# juros([Taxa de Juros, Tempo de Pagamento, Capital Inicial])

def juros(taxa, tempo, capital):
    juros_acrescido = capital * taxa * tempo
    montante = capital + juros_acrescido
    print("O juros é de: ", juros_acrescido)
    print("O montante foi de: ", montante)

juros(0.04,3,500)