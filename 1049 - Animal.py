c1 = str(input())
c2 = str(input())
c3 = str(input())

if c1 == "vertebrado":
    if c2 == "mamifero":
        if c3 == "onivoro":
            print("homem")
        else:
            print("vaca")
    if c2 == "ave":
        if c3 == "onivoro":
            print("pomba")
        else:
            print("aguia")
elif c1 == "invertebrado":
    if c2 == "inseto":
        if c3 == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    if c2 == "anelideo":
        if c3 == "onivoro":
            print("minhoca")
        else:
            print("sanguessuga")
            