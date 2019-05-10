cod = 1
a = 0
g = 0
d = 0
while cod != 4:
    cod = 0
    cod = int(input())
    if cod == 1:
        a += 1
    elif cod == 2:
        g += 1
    elif cod == 3:
        d += 1
print("MUITO OBRIGADO")
print("Alcool:", a)
print("Gasolina:", g)
print("Diesel:", d)
