#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e
#limitando o fatorial a números inteiros positivos e menores que 16.

resp = "s"
while resp == "s":
    num = int(input("Digite um número inteiro positivo e menor que 16: "))
    while num <= 0 or num > 16:
        num = int(input("Número iválido!\nDigite um número inteiro positivo e menor que 16: ")) 
    fato = 1

    for i in range(num):
        fato *= num
        num -= 1
    print(fato)
    resp = input("Deseja continuar? (S/N): ")
