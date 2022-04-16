""""
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
Depois modifique o programa para que ele mostre os números um ao lado do outro.
"""

for i in range(1,21):
    print (i)

for n in range (1, 21):
    print (n, end = " ")

# O que acontece aqui é que normalmente o print quebra a linha, e ao determinar esse end = " " ele diz que o print vai terminar com uma barra 
# de espaço, e não com uma quebra de linha. 
# Um lado "negativo" é que terá que quebrar a linha depois no próximo print