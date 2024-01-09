import random

number = random.randint(0, 100)
guess = False
count = 0

while (not (guess)):
    i = int(input("Rate eine Zahl: "))
    if (number == i):
        guess = True
    elif (number < i):
        print("lower ⏬⏬")
    elif (number > i):
        print("higher ⏫⏫")

    count += 1

print("Yay, mit nur " + str(count) + " Versuchen erraten 🐍🐍✨")