import random

print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.


Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

""")

random_int = random.randint(0,101)

choice = int(input("""Enter your choice: """))

if choice == 1:
    diff = "Easy"
    lives = 10
elif choice == 2:
    diff = "Medium"
    lives = 5
elif choice == 3:
    diff = "Hard"
    lives = 3



print(f"""Great! You have selected the {diff} difficulty level.
Let's start the game!""")

for i in range(lives + 1):
    guess = int(input("Enter your guess: "))
    if guess == random_int:
        print(f"Congratulations! You guessed the correct number in {i} attempts")
    if random_int > guess:
        print(f"Incorrect! The number is greater than {guess}")
    if random_int < guess:
        print(f"Incorrect! The number is greater than {guess}")

    if i > lives:
        print(f"print you are out of lives")
