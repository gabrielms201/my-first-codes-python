a = 13
b = 2

resto = a % b
while resto != 0:
  a = b
  b = resto
  resto = a % b

MDC = b
print(MDC)