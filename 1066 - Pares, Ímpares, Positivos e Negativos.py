par = 0
impar = 0
neg = 0
pos = 0

for i in range(0, 5):
    n = int(input())
    if n % 2 == 0:
        par += 1
    elif n % 2 != 0:
        impar = impar + 1
    if n > 0:
        pos = pos + 1
    elif n < 0:
        neg = neg + 1

print(par, "valor(es) par(es)")
print(impar, "valor(es) impar(es)")
print(pos, "valor(es) positivo(s)")
print(neg, "valor(es) negativo(s)")
