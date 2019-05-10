n = int(input())
n1 = 1
n2 = 1
n3 = 1

for x in range(n):
    print(n1, n2, n3)
    n1 += 1
    n2 = n1 * n1
    n3 = n2 * n1
    