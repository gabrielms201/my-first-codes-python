"""
Um posto de combustível vende três tipos de combustível: álcool, diesel e gasolina. O preço de cada litro 
dos  combustíveis  é  apresentado  na  tabela  abaixo.  Faça  um  programa  que  leia  um  caracter  que 
representa o tipo  de combustível comprado (a, d  ou  g) e a quantidade em litros.  O programa deve 
imprimir o valor em reais a ser pago pelo combustível

Alcool - 1,7997
Diesel - 0,9798
Gasolina - 2,1009
"""

#Combustíveis:
def gasolina(l):
  return (l*2.1009)
def alcool(l):
  return (l*1.7997)
def diesel(l):
  return (l*0.9798)

#Menu e cálculos:
def menu():
  global escolha;global litros
  print("\nTabela de preços:\nGasolina - 2,1009\nÁlcool - 1,79978\nDiesel - 0,9798\n")
  escolha = str.lower(input("Qual o combustível desejado?\n>Digite G para gasolina, A para álcool ou D para diesel: "))
  litros = float(input("Digite quantos livros de combustível você vai comprar:")) 
  calculos()
def calculos():
  if escolha == "g":
    total = gasolina(litros)
    print ("total é R$: %.2f" % total)
    continuar()
  elif escolha == "a":
    total = alcool(litros)
    print ("O total é R$: %.2f" % total)
    continuar()
  elif escolha == "d":
    total = diesel(litros)
    print ("O total é R$: %.2f" % total)
    continuar()
  else:
    print("Por favor, especifique o combustível desejado...")
    menu()
def continuar():
  continuar = str.lower(input("Deseja utilizar o programa novamente? (S/N) "))
  if continuar == "s":
    menu()

menu()