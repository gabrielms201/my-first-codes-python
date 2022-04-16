import json
import requests

def dolarApi(): #API JSON PARA COLETAR COTAÇÃO DOLAR
  response = requests.get("https://economia.awesomeapi.com.br/json/all/")
  info = json.loads(response.text)
  valorCompra = (info["USD"]["bid"])
  return(float(valorCompra))
def transformar(): #SISTEMA DE TRANSFORMAÇÃO 
  escolha = input("\n Digite RD para transformar reais em dólares ou digite DR para transformar dólares em reais (S para sair): ")
  if escolha == "RD" or escolha == "rd":
    valorDado = float(input("Digite o valor que deseja converter em dólares: "))
    conversao = (valorDado / dolarApi())
    resultado = print("{:.2f} Reais equivalem à {:.2f} Dólares".format(valorDado, conversao))
    return(resultado)
  elif escolha == "DR" or escolha == "dr":
    valorDado = float(input("Digite o valor que deseja converter em reais:\n"))
    conversao = (valorDado * dolarApi())
    resultado = print("{:.2f} Dólares equivalem à {:.2f} Reais".format(valorDado, conversao))
    return(resultado)
  elif escolha == "S" or escolha == "s":
    return False
  else:
    print("Especifique corretamente a transformação desejada.")
while True: #CHAMANDO O PROGRAMA 
  transformar()