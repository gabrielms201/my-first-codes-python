"""
numero = int(input('Digite um numero inteiro positivo: '))

# Extraindo a unidade
unidade = numero % 10

# Eliminando a unidade de nosso número
numero = (numero - unidade)/10

# Extraindo a dezena
dezena = numero % 10

# Eliminando a dezena do número original, fica a centena
numero = (numero - dezena)/10
centena = numero

# Fazendo ser inteiros
dezena = int(dezena)
centena = int(centena)
print(centena,'centena(s),',dezena,'dezena(s) e',unidade,'unidade(s)')

"""

n = int(input("Digite um número inteiro: ")) 
print(n) 
u = n%10 #Pegando a unidade 
d = (n // 10) % 10  #Pegando a dezena
c = (n // 100) % 10 #Pegando a centena
m = (n // 1000) % 10 #Pegando o milhar
x = (n // 10000) % 10 #Pegando n
print(n , "=", x, m, c, d, u) 


