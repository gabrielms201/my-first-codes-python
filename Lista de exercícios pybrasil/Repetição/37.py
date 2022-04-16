# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código,
#  sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
#  Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

menorAltura = 99999999
maiorAltura = 0
codigoMaiorAltura = 0
codigoMenorAltura = 0
somaAltura = 0

menorPeso = 99999999
maiorPeso = 0
codigoMenorPeso = 0
codigoMaiorPeso = 0 
somaPeso = 0

codigo = 1
qnt = 0

while codigo != 0:
    codigo = int(input("Digite o seu código: (0 para sair): "))
    if codigo == 0: break
    altura = float(input("Digite a sua altura: (em metros) "))
    peso = float(input("Digite o seu peso: (em kg) "))
    
    if peso < menorPeso:
        menorPeso = peso
        codigoMenorPeso = codigo
    if peso > maiorPeso:
        maiorPeso = peso
        codigoMaiorPeso = codigo
    
    if altura < menorAltura:
        menorAltura = altura
        codigoMenorAltura = codigo
    if altura > maiorAltura:
        maiorAltura = altura
        codigoMaiorAltura = codigo
    
    qnt += 1
    somaAltura += altura
    somaPeso += peso

mediaAltura = somaAltura/qnt
mediaPeso = somaPeso/qnt

print("\nCliente mais alto: Código: %d Altura: %.2fm" % (codigoMaiorAltura, maiorAltura))
print("Cliente mais baixo: Código: %d Altura: %.2fm" % (codigoMenorAltura, menorAltura))
print("Cliente mais gordo: Código: %d Peso: %.2fkg" % (codigoMaiorPeso, maiorPeso))
print("Cliente mais magro: Código: %d Peso: %.2fkg" % (codigoMenorPeso, menorPeso))
print("Média de peso: %.2f\nMédia de alturas: %.2f" % (mediaPeso, mediaAltura))