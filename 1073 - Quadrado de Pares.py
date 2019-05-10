n = int(input())
i = 1

for x in range(n):
    if i % 2 == 0:
        aux = i * i
        print("{}^2 = {}".format(i,aux))
    i = i + 1
    