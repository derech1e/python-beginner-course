import random

number = random.randint(0, 100)

zahl = 101
i = 0

while (number != zahl):
    zahl = int(input("Gib eine Zahl ein: "))
    i += 1 # <=> i = i + 1
    if (zahl < number):
        print("Zahl ist zu klein")

    elif (zahl > number):
        print("Zahl ist zu groß")

    else:
        print("Versuche: " + str(i))
        print("Zahl war " + str(number))
