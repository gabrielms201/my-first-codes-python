def valor_omissao(valor):
    if valor==" ":
        return int(1)
    else:
        return condicao(valor)

def condicao(valor):
    if valor <1:
        return int(1)
    elif valor >20:
        return int(20)
    else:
        return valor

def linhas(qnt):
    ponta = "+"
    meio = "-"
    print("%s%s%s" % (ponta,meio*qnt,ponta))

def colunas(qnt, linhas):
    ponta = "|"
    meio = " "
    for i in range(0, qnt):
        print("%s%s%s" % (ponta,meio*linhas,ponta))

def desenho(linha, coluna):
    linhas(linha)
    colunas(coluna, linha)
    linhas(linha)

valorlinha = int(input("Digite a quantidade de linhas (min 1, máx 20): "))
valorcoluna = int(input("Digite a quantidade de colunas (min 1, máx 20): "))
desenho(valor_omissao(valorlinha),valor_omissao(valorcoluna))

