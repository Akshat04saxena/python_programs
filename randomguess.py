import random

r = random.randint(1, 20)

while True:
    inp = int(input("Enter a number :"))
    if inp < r:
        print("wrong guess , Try a greater number")
    elif inp > r:
        print("wrong guess , Try a smaller number")
    else:
        print("Congrats , you've guessed the number")
        break
