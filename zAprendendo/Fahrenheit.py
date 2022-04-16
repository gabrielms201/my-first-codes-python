"""
Perguntar se quer celsius ou fahrenheit
Escolher o valor
Converter

"""

escolhaGrandeza = input("\nDigite FC para converter Fahrenheit em Celsius ou CF para transformar Celsius em Fahrenheit: ")
if escolhaGrandeza == "FC" or escolhaGrandeza == "fc":
  valorFtoC = float(input("Digite seu valor para converter para Celsius: "))
  print(valorFtoC,"°F equivalem à", ((valorFtoC-32)*5)/9,"°C")
elif escolhaGrandeza == "CF" or escolhaGrandeza == "cf":
  valorCtoF = float(input("Digite o seu valor para converter à Fahrenheit: "))
  print(valorCtoF, "°C equivalem à", (valorCtoF)*9/5 + 32, "°F")
else:
  print("Especifique qual a transformação desejada")