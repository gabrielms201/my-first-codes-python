"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite 
a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""

usuario = input("Digite o seu usuário: ")
senha = input("Digite a sua senha: ")

while usuario == senha:
    print("A senha não deve ser igual ao nome de usuário!")
    usuario = input("Digite o seu usuário: ")
    senha = input("Digite a sua senha:")

print("Bem vindo, %s" % usuario)

