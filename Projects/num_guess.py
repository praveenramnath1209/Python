import random

lst = (1,2,3,4,5,6,7,8,9,10)

n = int(input("Enter a number (1 to 10): "))

if n >= 1 and n <= 10:
    x = random.choice(lst)
    print("Random number was:", x)

    if n == x:
        print("Correct Guess!")
    elif abs(n - x) == 1:
        print("So close!")
    else:
        print("Wrong Guess!")
else:
    print("Invalid input! Please enter a number from 1 to 10.")
