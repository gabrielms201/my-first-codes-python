#Dictionary
a = { 
  "Nome":"Ricardo",
  "Idade":"19",
  "Aulas":["Fundamentos", "Algoritmos", "Circuitos"]
}
print("Nome = {}".format(a["Nome"]))

# Array / List
b = ["verde", "amarelo", "azul"] ; b[0]="laranja" # : Dados ordenados e podem alterar
print(f"B = {b[0]}")

#Turple
c = ("verde", "amarelo", "azul") # :  Dados ordenados e não podem alterar
print(f"C = {c[0]}")

#Complex
d = complex(1,2) #Número Complexo

#Range
e = range(1,100,2) #Range : Esse 2 simboliza que o número vai de 2 em 2

#Sets:
f = {5,3,2,7,8,9,5,3} # Set : Ordena os valores (apenas números) e exclui os repetidos
print(f) # Detalhes importantes sobre sets: "Set items are unordered, unchangeable, and do not allow duplicate values"
g = frozenset({5,3,2,7,8,9,5,3}) # Frozenset : Bloqueia, congela o set


"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered and changeable. No duplicate members.
DETALHE: Quando se referem à ordem, se referem à ordem da escrita

"""