# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). 
# Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
# Maior e Menor Acerto;
# Total de Alunos que utilizaram o sistema;
# A Média das Notas da Turma
# Gabarito da Prova:

# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A

menor = 9999
maior = 0
pontos = 0
contagem = 0
soma = 0
while True:

    contagem += 1
    primeira = input("Digite a resposta da questão 1: ").upper()
    if primeira == "A":
        pontos += 1
    segunda = input("Digite a resposta da questão 2: ").upper()
    if segunda == "B":
        pontos += 1
    terceira = input("Digite a resposta da questão 3: ").upper()
    if terceira == "C":
        pontos += 1
    quarta = input("Digite a resposta da questão 4: ").upper()
    if quarta == "D":
        pontos += 1
    quinta = input("Digite a resposta da questão 5: ").upper()
    if quinta == "E":
        pontos += 1
    sexta = input("Digite a resposta da questão 6: ").upper()
    if sexta == "E":
        pontos += 1
    setima = input("Digite a resposta da questão 7: ").upper()
    if setima == "D":
        pontos += 1
    oitava = input("Digite a resposta da questão 8: ").upper()
    if oitava == "C":
        pontos += 1
    nona = input("Digite a resposta da questão 9: ").upper()
    if nona == "B":
        pontos += 1
    decima = input("Digite a resposta da questão 10: ").upper()
    if decima == "A":
        pontos +=1
        
    if pontos < menor:
        menor = pontos
    if pontos > maior:
        maior = pontos
    soma += pontos
    print("Você acertou: %d" % pontos)
    pontos = 0
    sair = str.lower(input("Deseja sair? (S/N)"))
    if sair == "s":
        break

media = soma/contagem
print("Maior acerto: %.2f Menor acerto: %.2f\nTotal de alunos: %d\nMédia de notas: %.2f " % (maior, menor, contagem, media))