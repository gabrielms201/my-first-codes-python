"""

Um pescador comprou um computador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca
do Estado de São Paulo (50 quilos), deve pagar uma multa de R$ 4,00 por quilo excedente.
Escreva um programa que leia o peso de peixes, e verifique se há excesso. Se houver, determine
o peso excedente e o valor da multa. Caso contrário, mostrar “Dentro do regulamento”.


"""
pesoPeixe = int(input("Digite o peso do peixe:\n"))
regulamento = 50
excedente = pesoPeixe - regulamento
multa = (excedente*4)

if pesoPeixe > regulamento:
  print(f"\nSeu peixe excede {excedente}kg do regulamento, que é {regulamento}kg, logo você deverá pagar uma multa de R$:{multa}")
else:
  print(f"Dentro do regulamento")
  
