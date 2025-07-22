import random

count = 0
num = int(input("Enter number of dice to roll: "))

while True:
    n = input("Do you want to roll the dice (y/n): ").lower()

    if n == "y":
        print("Rolling the dice...")
        for i in range(num):
            x = random.randint(1, 6)
            print(f"Dice {i+1}: {x}")
            count += 1
        print(f"Total rolls so far: {count}\n")
    elif n == "n":
        print(f"Goodbye! You rolled the dice {count} times.")
        break
    else:
        print("Invalid input, please select again.")
