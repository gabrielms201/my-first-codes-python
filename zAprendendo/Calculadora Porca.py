import os
def calculadora():
  while True:
    print("\n---------------------------------------")
    print("           Calculadora")
    print("1- Soma")
    print("2- Subtração")
    print("3- Divisão")
    print("4- Sair")
    print("---------------------------------------")

    escolha = input("\nDigite sua escolha:\n")
    if escolha == "4":
      os.system('cls' if os.name == 'nt' else 'clear')
      break

    else:
      num1 = float(input("Digite seu primeiro número:\n"))
      num2 = float(input("Digite o seu segundo número:\n"))

    if escolha == "1":
      print(f"\nA soma é: {num1 + num2}")
    elif escolha == "2":
      print(f"A subtração é: {num1 - num2}")
    elif escolha == "3":
      print(f"A divisão é: {num1/num2}")

calculadora()