n = int(input())
i = 0
f = 0

for x in range(n):
    n1 = int(input())
    if n1 >= 10 and n1 <= 20:
        i += 1
    else:
        f += 1

print(i, "in")
print(f, "out")
