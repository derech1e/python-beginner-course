high = 100
low = 0

guess = 0

correct = False
count = 0

while (correct == False):
    count += 1
    guess = int((low + high) / 2)
    inp = input("Is your number " + str(guess) + "\n")
    if (inp == 'c'):
        print("Yay, " + str(count) + ". try")
        correct = True
    elif (inp == "l"):
        high = guess
    elif (inp == "h"):
        low = guess
