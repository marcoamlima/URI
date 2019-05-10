quant = int(input())

for x in range(quant):
    n = int(input())
    if n == 0:
        print("NULL")
    elif n % 2 == 0:
        if n > 0:
            print("EVEN POSITIVE")
        else:
            print("EVEN NEGATIVE")
    elif n % 2 != 0:
        if n > 0:
            print("ODD POSITIVE")
        else:
            print("ODD NEGATIVE")
            