I = 1
J = 7

while I < 10:
    for x in range(3):
        print("I=%.0f" % I, "J=%.0f" % J)
        J += -1
    I += 2
    J = I + 6
    