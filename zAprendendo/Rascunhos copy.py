alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X","Y","Z"]

final = input("Digite a última letra a ser gerada: ").upper()
indexfinal = alfabeto.index(final)

espaco = indexfinal+1
espaco2 = 1
print(" "*espaco + " "+ alfabeto[0])
print()
for i in range(0, indexfinal):
    print(espaco * " " + alfabeto[i+1] + (" " * espaco2) + alfabeto[i+1])
    print()
    espaco -= 1
    espaco2 += 2
    
espaco += 1
espaco2 -= 2
for i in range(indexfinal-2, -1, -1):
    espaco += 1
    espaco2 -= 2
    print(espaco * " " + alfabeto[i+1] + (" " * espaco2) + alfabeto[i+1])
    print()

print(" "*espaco + " " + alfabeto[0])
