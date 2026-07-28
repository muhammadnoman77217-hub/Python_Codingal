b = 5
print("in this game the computer will gues the number that is given by the user and u will have 5 attempts")
guess = int(input("inter a number : "))
score = 1
if guess == 5:
    print("You guessed correctly")
    print("score = 1")
elif guess < 5:
    print("cold")
    int(input("try again"))
    print("score = 11")
elif guess > 5:
    print("hot")
    int(input("try again"))
    print("score = -2")
elif guess > 3:
    print("warm")
    int(input("try again"))
    print("score = -3")
elif guess > 2:
    print("ice")
    int(input("try again"))
    print("score = -4")