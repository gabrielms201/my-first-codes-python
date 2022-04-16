"""

8) (Problema 19) - JSEDEX - Sedex
A Copa do Mundo de 2018 será realizada na Rússia. Bolas de futebol são muito fáceis de transportar,
já que elas saem das fábricas vazias e só são enchidas somente pelas lojas ou pelos consumidores
finais.
Infelizmente o mesmo não pode ser dito das bolas de boliche. Como elas são completamente
sólidas, elas só podem ser transportadas embaladas uma a uma, em caixas separadas.
A SBC - Só Boliche Cascavel - é uma fábrica de bolas de boliche que trabalha somente através de
encomendas e envia todas as bolas por SEDEX. Como as bolas têm tamanhos diferentes, a SBC tem
vários tamanhos de caixas diferentes para transportá-las
Tarefa
Escreva um programa que, dado o diâmetro de uma bola e as 3 dimensões de uma caixa (altura,
largura e profundidade), diz se a bola de boliche cabe dentro da caixa ou não.
Entrada
A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 10.000) que indica o diâmetro da bola de
boliche. A segunda linha da entrada contém 3 números inteiros separados por um espaço cada: a
altura A (1 ≤ A ≤ 10.000), seguida da largura L (1 ≤ L ≤ 10.000) e da profundidade P (1 ≤ P ≤ 10.000).
Saída
Seu programa deve imprimir uma única linha, contendo a letra 'S' caso a bola de boliche caiba dentro
da caixa ou 'N' caso contrário

3
"""

import math

diametro = int(input("Digite o diâmetro da bola: "))
altura,largura,profundidade = (input("Digite, respectivamente, a altura, largura e profundidade da caixa.").split(" "))
altura = int(altura)
largura = int(largura)
profundidade = int(profundidade)
raio = diametro / 2

if diametro >= 1 and diametro <=10000 and altura >=1 and altura <=10000 and largura >=1 and largura <=10000 and profundidade >= 1 and profundidade <= 10000:
  volumeCaixa = altura * largura * profundidade 
  volumeBola = (4*math.pi*(math.pow(raio,3)))/(3)
  if volumeBola <= volumeCaixa:
    print("S")
  else:
    print("N")
else: 
  print ("Os valores inseridos devem estar entre 1 e 10 000...")


