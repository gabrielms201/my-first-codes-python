"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:

"""

def calculadorImposto(salarioBruto):
  imposto = (salarioBruto*0.11)
  inss = (salarioBruto*0.08)
  sindicato = (salarioBruto*0.05)
  salarioLiquido = salarioBruto	- (imposto + inss + sindicato)
  nomeUsuario = input("Digite seu nome:")
  print("Bem vindo,", nomeUsuario)
  print("Você pagou", inss, "ao INSS", imposto, "de imposto de renda", "e", sindicato, "ao sindicato")
  print("Sua renda liquida foi de:", salarioLiquido)
calculadorImposto(15000)

