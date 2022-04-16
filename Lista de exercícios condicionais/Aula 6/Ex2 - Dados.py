""""
Esse é o jogo dos dados, muito usado em Las Vegas nos cassinos, aposte em um 
número que seja o resultado da soma deles e ganhe o seu dinheiro. Crie duas variáveis 
para representar os dados e uma para sua aposta, crie uma para armazenar o resultado 
e faça a verificação. 
"""
import random

dado1= random.randint(1,6)
dado2= random.randint(1,6)
soma = dado1 + dado2

inputNum = int(input("Digite o valor da sua aposta da soma de dois dados (6 faces) "))
print(soma)
if soma == inputNum :
  print("Você venceu!")
else:
  print("Você perdeu!")