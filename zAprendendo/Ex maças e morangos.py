"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""
morango = float(input("Quantos kg de morango deseja comprar? "))
maca = float(input("Quantos kg de maçã deseja comprar? "))
desconto = 0 

if morango > 5:
    valor_morango = 2.2*morango
else:
    valor_morango = 2.5*morango

if maca > 5:
    valor_maca = 1.5*maca
else:
    valor_maca = 1.8*maca

valor_total = valor_morango + valor_maca
quantidade_total = morango + maca

if quantidade_total > 8 or valor_total > 25:
    desconto = 0.10*valor_total
valor_total = valor_morango + valor_maca - desconto
print("================================================\nMaçãs: R$: %.2f\nMorangos: R$: %.2f\nDesconto: R$: %.2f\n\nValor Total: R$: %.2f\n================================================"
 % (valor_maca, valor_morango, desconto, valor_total))