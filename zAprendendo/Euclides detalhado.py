a = 16
b = 5

resto = a % b        # 1
while resto != 0:    

  a = b              #a = 5
  b = resto          #b = 1
  resto = a % b      #resto = 5 % 1 = 0 

mdc = b              #mdc = 1
print(mdc)