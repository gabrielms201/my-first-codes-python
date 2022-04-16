# Faça um programa, com uma função que necessite de um argumento.
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def validador(a):
    if a > 0:
        return("P")
    elif a <= 0:
        return("N")
num = float(input("Digite o número: "))
print(validador(num))