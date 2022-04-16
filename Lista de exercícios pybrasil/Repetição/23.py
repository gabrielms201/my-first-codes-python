# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.


div = 0
n = int(input("Digite um número: "))
for i in range(2,n):
    for j in range(2,i):
        if i%j == 0:
            num = "Primo"
            div+=1
            break
    else: 
        print(i)
print("Número de divisões executadas:", div)


