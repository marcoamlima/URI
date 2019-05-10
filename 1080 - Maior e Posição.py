n = 0
pos = 0
maior = n
for x in range(100):
    n = int(input())
    if (n > maior):
        maior = n
        pos = x + 1
print(maior)
print(pos)
