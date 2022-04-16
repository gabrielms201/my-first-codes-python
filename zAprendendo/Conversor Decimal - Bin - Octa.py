numInput = int(input("Digite o seu número em decimal: "))
def conversorBin():
  fonte = numInput
  base = 2
  resto = fonte%base
  destino = []
  quo = fonte // base
  pos = 0
  while quo != 0:
    quo
    resto = fonte%base
    pos += -1
    destino.insert(pos,resto)
    quo = fonte // base
    fonte = quo
  return destino
def conversorOct():
  fonte = numInput
  base = 8
  resto = fonte%base
  destino = []
  quo = fonte // base
  pos = 0
  while quo != 0:
    quo
    resto = fonte%base
    pos += -1
    destino.insert(pos,resto)
    quo = fonte // base
    fonte = quo
  return destino

print(conversorBin())
print(conversorOct())


