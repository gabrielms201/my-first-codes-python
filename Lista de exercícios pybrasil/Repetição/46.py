# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados.
#  O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a 
# média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. 
# Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

# Atleta: Rodrigo Curvêllo
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Melhor salto:  6.5 m
# Pior salto: 5.3 m
# Média dos demais saltos: 5.9 m
# Resultado final:
# Rodrigo Curvêllo: 5.9 m
melhor = pior = media = contagem = soma = mediaTotal = 0
ordem = "Primeiro","Segundo","Terceiro","Quarto","Quinto"

while True:
    nome = input("\nDigite o nome do Atleta: ")
    if nome == "" or nome == " ": break
    for i in range(0,5):
        salto = float(input("%s Salto: " % ordem[i]))
        contagem += 1
        if salto > melhor:
            melhor = salto
        if salto < pior or contagem == 1:
            pior = salto
        soma += salto
    media = ((soma-pior)- melhor)/3
    mediaTotal = soma/5
    print("\n\nMelhor Salto: %.2f\nPior Salto: %.2f\nMédia dos demais saltos: %.2f\nResultado Final: %s:%.2f" % (melhor, pior, media, nome, mediaTotal))


