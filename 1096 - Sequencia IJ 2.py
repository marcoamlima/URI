I = 1
J = 7

while I < 10:
    print("I=%.0f" % I, "J=%.0f" % J)
    if J == 5:
        I += 2
        J = 7
    else:
        J += -1
        