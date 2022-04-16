"""
O  Jogo  do  par  ou  ímpar  é  usado  onde  duas  pessoas  jogam 
geralmente para decidir um impasse, cada um escolhe entre par ou ímpar e 
mostra o seu número, a soma entre eles resulta em um número par ou ímpar 
e assim é decidido o vencedor. Aqui faremos com a máquina, ela escolherá 
um número randômico entre 0 e 10 e você escolherá o seu. Vamos ver quem 
é o vencedor!!!!
"""


import random
randNum = random.randint(0,10)
escolha = input("Você aposta em par ou impar? ")
inputNum = int(input("Digite um valor de 0 a 10: "))
soma = randNum + inputNum


print("A escolha de seu oponente foi: {}, totalizando {}".format(randNum, soma))

if soma % 2 == 0:
  if escolha == "par" or escolha == "Par":
    print("Você venceu!")
  else:
    print("Você perdeu")
else:
  if escolha == "impar" or escolha == "ímpar" or escolha == "Impar":
    print("Você venceu!")
  else:
    print("Você perdeu!")
