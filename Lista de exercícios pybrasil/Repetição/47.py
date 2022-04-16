# Em uma competição de ginástica, cada atleta recebe votos de sete jurados. 
# A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes.
#  Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a
#  descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. 
# Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Aparecido Parente
# Nota: 9.9
# Nota: 7.5
# Nota: 9.5
# Nota: 8.5
# Nota: 9.0
# Nota: 8.5
# Nota: 9.7

# Resultado final:
# Atleta: Aparecido Parente
# Melhor nota: 9.9
# Pior nota: 7.5
# Média: 9,04

melhor = pior = media = contagem = soma = mediaTotal = 0
ordem = "Primeira","Segunda","Terceira","Quarta","Quinta","Sexta","Sétima"

while True:
    nome = input("\nDigite o nome do Atleta: ")
    if nome == "" or nome == " ": break
    for i in range(0,7):
        nota = float(input("%s nota: " % ordem[i]))
        contagem += 1
        if nota > melhor:
            melhor = nota
        if nota < pior or contagem == 1:
            pior = nota
        soma += nota
    media = ((soma-pior)- melhor)/5
    mediaTotal = soma/7
    print("\n\nResultado Final: %s\nMelhor Nota: %.2f\nPior Nota: %.2f\nMédia das demais Notas: %.2f\n" % (nome, melhor, pior, media))

