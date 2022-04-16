# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade
# da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

n = int(input("Quantas pessoas existem na turma? "))
soma = 0
qtd = n

while n > 0:
    idade = int(input("Digite a idade do sujeito: "))
    soma += idade
    n-=1 
media = soma/qtd

if media >0 and media <=25:
    turma = "A turma é jovem"
elif media >=26 and media <= 60:
    turma = "A turma é adulta"
elif media > 60:
    turma = "A turma é idosa"
print(turma)
