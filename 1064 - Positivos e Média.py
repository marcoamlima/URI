pos = 0
aux = 0
media = 0
for x in range(6):
    n = float(input())
    if n > 0:
        pos = pos + 1
        aux = aux + n
media = aux / pos
print(pos, "valores positivos")
print("%.1f"%media)
