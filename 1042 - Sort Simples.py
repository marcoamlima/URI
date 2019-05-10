n1, n2, n3 = map(int, input().split())

v = [0, 0, 0]
if (n1 < n2) and (n1 < n3):
    v[0] = n1
    if n2 < n3:
        v[1] = n2
        v[2] = n3
    else:
        v[1] = n3
        v[2] = n2
elif (n2 < n1) and (n2 < n3):
    v[0] = n2
    if n1 < n3:
        v[1] = n1
        v[2] = n3
    else:
        v[1] = n3
        v[2] = n1
elif (n3 < n1) and (n3 < n2):
    v[0] = n3
    if n2 < n1:
        v[1] = n2
        v[2] = n1
    else:
        v[1] = n1
        v[2] = n2
elif n1 == n2 == n3:
    v[0] = n1
    v[1] = n2
    v[2] = n3

print(v[0])
print(v[1])
print(v[2])

print()

print(n1)
print(n2)
print(n3)
