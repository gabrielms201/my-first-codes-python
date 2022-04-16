"""
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
"""

n = 7
num1 = 0
num2 = 1

while n > 0:
    print(num1)
    print(num2)
    num1 = num1+num2
    num2 = num1+num2
    n -= 2
    