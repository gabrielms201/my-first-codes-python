# Fundamentos Criptografia
# Ricardo Ruiz
def criptografar():
    alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    texto = input("Digite o texto para criptografar: ").upper()
    chave = int(input("Digite a chave (número inteiro)"))
    for e in texto:
        letra_index = int(alfabeto.index(e))
        cripto = alfabeto[(letra_index)+chave]
        print(cripto, end="")
    menu()
def decriptografar():
    alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    texto = input("Digite o texto para decriptografar: ").upper()
    chave = int(input("Digite a chave (número inteiro)"))
    for e in texto:
        letra_index = int(alfabeto.index(e))
        cripto = alfabeto[(letra_index)-chave]
        print(cripto, end="")
    menu()

def menu(): 
    escolha = input("Você deseja criptografar ou decriptografar? (S para sair) (C/D)").upper()
    if escolha == "C":
        criptografar()
    elif escolha == "D":
        decriptografar()
    elif escolha == "S":
        exit()
    else:
        print("Escolha incorreta! Tente novamente")
        menu()
menu()

