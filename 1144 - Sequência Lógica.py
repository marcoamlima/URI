n = int(input())
a = 1

for i in range(1,(n*2)+1):
    if(i%2 == 0):
        print("%d %d %d" %(a,(a**2)+1,(a**3)+1))
        a += 1
    else:
        print("%d %d %d" %(a,a**2,a**3))
        