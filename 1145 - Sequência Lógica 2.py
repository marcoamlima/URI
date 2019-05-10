x, y = map(int, input().split())
cont = 1
for z in range(1, (int((y/x))+1)):
    f = ""
    for t in range(x):
        f += str(cont) + " "
        cont += 1
    print(f[:-1])
    