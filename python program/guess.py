import random

r = random.randint(1, 20)
while True:
    inp = int(input())
    if inp < r:
        print("wrong guess, try a greater number")
    elif inp > r:
        print("wrong guess, try a smaller number")
    else:
        print("congrats, you ve guessed the number")
        break
