import random

emojis = {
    "r": "🪨",
    "p": "📄",
    "s": "✂️"
}

choices = ('r', 'p', 's')

while True:
    ip = input("Rock, Paper, or Scissors? (r/p/s): ").lower()
    cc = random.choice(choices)

    if ip not in choices:
        print("Invalid Input! Please select r, p, or s.")
        continue

    print(f"You chose {emojis[ip]}")
    print(f"Computer chose {emojis[cc]}")

    if ip == cc:
        print("It's a Draw")
    elif (ip == "s" and cc == "p") or (ip == "r" and cc == "s") or (ip == "p" and cc == "r"):
        print("You won!")
    else:
        print("Computer won!")

    cont = input("Do you want to play again? (y/n): ").lower()
    if cont != 'y':
        print("Thanks for playing!")
        break
