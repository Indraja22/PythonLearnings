import random

generated_random_number = random.randrange(0, 26)
counter = 0
user_guess = int(input("Guess the number : "))

if user_guess == generated_random_number:
    print(f"You Guessed The Right Number {user_guess} In {counter} Attempt")
    quit()

while user_guess != generated_random_number:
    if user_guess > generated_random_number:
        print("Too high!")
        counter += 1
    elif user_guess < generated_random_number:
        print("Too low!")
        counter += 1
    user_guess = int(input("Guess the number : "))

print(f"Correct guess after {counter} attempts! The Number Is : {user_guess}")
