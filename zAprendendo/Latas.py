""""

Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.


"""

#Input
tamanhoArea = 74845545
#Processamento
litrosNecessarios = tamanhoArea / 3
if tamanhoArea % 18 == 0:
  latasNecessarias = litrosNecessarios / 18
else:
  latasNecessarias =int((litrosNecessarios / 18)+1)
valorTotal = (latasNecessarias * 80)
#Output
print(latasNecessarias, valorTotal)