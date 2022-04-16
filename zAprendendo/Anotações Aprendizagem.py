#Formatação de Strings
a = 32
b = 44
print("O valor de a é igual a: {a} e b é igual a: {b}".format(a=a,b=b))
print("O valor de a é igual a: {0} e b é igual a: {1}".format(a, b))
print(f"O valor de a é igual a: {a} e b é igual a: {b}")
print("O valor de a é igual a:", a, "e b é igual a:", b)
#Todo float ocupa no minimo 6 casas decimais ao formatar. Ex:
print("Tamanho = {:f}".format(5))


#Organização de Dados
data = [9, 2, 43, 18, 32, 77, 99] 
print("{d[3]} e {d[6]}".format(d=data))
print("{0[3]} e {0[6]}".format(data))
print(f"{data[3]} e {data[6]}")
print(data[3], "e", data[6])

#Reconhecer tipo de dado
idade = 20.5
print("idade", type(idade))
print(f"A idade é {type(idade)} caralho")

#Pegar um numero em um intervalo
import random
for i in range(10):
  num = random.randint(1,13)
  print (num)

#Converter caracteres para inteiro ascii:
ord("A")
#Inverso:
chr(65)



#Split de String > Você dá um valor para que ele realize um corte em determinado caractere, e retorna um array. Nesse caso o caractere desejado foi o barra de espaço
curso = "Curso de Python"
print(curso.split(" "))
print(curso.split(" ")[0])
print(curso.split(" ")[1])
print(curso.split(" ")[2])