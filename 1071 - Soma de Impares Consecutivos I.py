X = int(input())
Y = int(input())
soma = 0
if X > Y:
    m = X
    mn = Y
else:
    m = Y
    mn = X
for x in range(mn + 1, m):
    if x % 2 != 0:
        soma = soma + x
print(soma)
