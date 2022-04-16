"""
Perguntar se quer celsius ou fahrenheit
Escolher o valor
Converter

"""
while True: 
  escolhaGrandeza = input("\nDigite FC para converter Fahrenheit em Celsius ou CF para transformar Celsius em Fahrenheit:")
  if escolhaGrandeza == "FC" or escolhaGrandeza == "fc":
    valorFtoC = float(input("Digite seu valor para converter para Celsius: "))
    print(f"\n{valorFtoC}°F equivalem à {(((valorFtoC-32)*5)/9):.2f}°C")
  elif escolhaGrandeza == "CF" or escolhaGrandeza == "cf":
    valorCtoF = float(input("Digite o seu valor para converter à Fahrenheit: "))
    print(f"\n{valorCtoF}°C equivalem à {((valorCtoF)*9/5 + 32):.2f}°F")
  else:
    print("Especifique qual a transformação desejada")
  sair = input("Digite x para sair, ou aperte enter para continuar\n")
  if sair == "x" or sair == "X":
    break
