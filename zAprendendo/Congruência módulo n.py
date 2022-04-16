# X cong y mod n
# X 0 mod2 > 2(x-0
# x  cong modn quando x e y deixam o mesmo resto na divisão por n
#[-7,-2,3,8]

for x in range(-50,50):
  y = 3
  n = 5
  restox = x%n
  restoy = y%n
  if restox == restoy:
    print(x)

