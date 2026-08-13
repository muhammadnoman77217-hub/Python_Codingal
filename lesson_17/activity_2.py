import random   #importing module

number = int(random.randint(0,9))   # random in-built function
print("I will generate a number from 0 to 9, and you have to guess a number one digit at a time.")

while True:
    guess = int(input("Make a guess : "))
    if guess == number:
        print(f"you won the number is {guess}")
        break
    elif guess>number:
        print("you guessed too high please pich a smaller number")
    else:
        print("you guessed too low please pick a larger number")

print("thank you for playing")