# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. 
# Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

qnt = int(input("Quantos alunos? "))
menor = 999999
maior = 0 
numeroMaior = 0
numeroMenor = 0 

for i in range(qnt):
    numero = int(input("Digite o seu número: "))
    altura = float(input("Digite a sua altura: "))
    if altura < menor:
        menor = altura
        numeroMenor = numero
    if altura > maior:
        maior = altura
        numeroMaior = numero


print("Número maior: %d | Altura maior: %.2f\nNúmero menor: %d | Altura menor: %.2f " % (numeroMaior, maior, numeroMenor, menor))