def berechne_ggt(a, b):
    while b:
        a, b = b, a % b
    return a

zahl_1 = int(input("Geben sie die erste Zahl: "))
zahl_2 = int(input("Geben sie die zweite Zahl: "))

ggt = berechne_ggt(zahl_1, zahl_2)

print("der ggt ist " +str(ggt))
