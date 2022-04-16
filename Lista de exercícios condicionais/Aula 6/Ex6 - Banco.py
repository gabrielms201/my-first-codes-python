"""
Um banco concederá um crédito especial aos seus clientes de acordo com o saldo médio no último ano. 
Receba o saldo médio de um cliente, calcule e mostre o valor do crédito, de acordo com a tabela a seguir. 

Acima de R$ 4.000,00  30% do saldo médio 
De R$ 3.000,01 a R$ 4.000,00  25% do saldo médio 
De R$ 2.000,01 a R$ 3.000,00  20% do saldo médio 
Até R$ 2.000,00  10% do saldo médio 

"""



def trintaPorcento(s):
  return (s*0.30)
def vinteCincoPorcento(s):
  return (s*0.25)
def vintePorcento(s):
  return (s*0.20)
def dezPorcento(s):
  return (s*0.10)

def verificador():
  salario = float(input("Digite o seu salário: ").replace(",","."))
  bonus = 0
  if salario > 4000:
    bonus = trintaPorcento(salario)
    total = salario + bonus
    print("Seu bônus será de R$:{:.2f} (30%)\nTotalizando R$:{:.2f}".format(bonus, total).replace(".",","))
  elif salario >= 3000.01 and salario <= 4000:
    bonus = vinteCincoPorcento(salario)
    total = salario + bonus
    print("Seu bônus será de R$:{:.2f} (25%)\nTotalizando R$:{:.2f}".format(bonus, total).replace(".",","))
  elif salario >= 2000.01 and salario <= 3000:
    bonus = vintePorcento(salario)
    total = salario + bonus
    print("Seu bônus será de R$:{:.2f} (20%).\nTotalizando  R$:{:.2f}".format(bonus, total).replace(".",","))  
  else:
    bonus = dezPorcento(salario)
    total = salario + bonus
    print("Seu bônus será de R$:{:.2f} (10%).\nTotalizando  R$:{:.2f}".format(bonus, total).replace(".",","))

verificador()