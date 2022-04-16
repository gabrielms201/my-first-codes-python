"""
Sabendo como funciona o jogo crie uma variável para cada jogador que deve armazenar a opção escolhida 
pela criança (Pedra, Papel ou Tesoura) e apresente o resultado da jogada. 
"""
import random
print("------------------------------------------------")
print("\nVocê está jogando pedra, papel ou tesoura...\n")
escolha = str.lower(input("Digite sua escolha: "))
oponente = random.choice(["Pedra", "Papel", "Tesoura"])


print("A escolha de seu oponente foi: {}\n".format(oponente))
print("Resultado:")
#Usuário escolhe pedra:
if escolha == "pedra":
  if oponente == "Tesoura":
    print("Você ganhou!")
  elif oponente == "Papel":
    print("Você perdeu!")
  else:
    print("Empate!")
#Usuário escolhe papel:
if escolha == "papel":
  if oponente == "Pedra":
    print("Você ganhou!")
  elif oponente == "Tesoura":
    print("Você perdeu!")
  else:
    print("Empate!")
#Usuário escolhe tesoura:
if escolha == "tesoura":
  if oponente == "Papel":
    print("Você ganhou!")
  elif oponente == "Pedra":
    print("Você perdeu!")
  else:
    print("Empate!")
print("\n------------------------------------------------")
