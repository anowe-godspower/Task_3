import random

guess = input("Guess The Number: ")
number = random.randint(1, 9)

while(int(guess) != number):
    # print(guess)
    # print(number)
    print("Wrong, Try Again.")
    guess = input("Guess The Number: ")

print(f"Well Guessed, number is {guess}.")
# print(number)