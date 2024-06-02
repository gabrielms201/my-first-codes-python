def Login(inputUser, inputPassword):
  correctUser = "pdrzinho" 
  correctPassword = "senha"
  if correctUser == inputUser and correctPassword == inputPassword:
    print("Bem vindo, ", correctUser)
  elif correctPassword != inputPassword and correctUser != inputUser :
    print("Usuário e senha incorretos")
  elif correctUser != inputUser:
    print("Usuário Incorreto. (OBS: Letras maíusculas diferem-se de letras minúsculas)")
  elif correctPassword != inputPassword:
    print("Senha Incorreta. (OBS: Letras maiúsculas diferem-se de letras minúsculas)")
usuarioDigitado = input("Digite o seu usuário: ")
senhaDigitada = input("Digite a sua senha: ")
Login(usuarioDigitado, senhaDigitada)
