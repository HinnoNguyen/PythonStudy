import random

# Define symbols
symbols = ["🍒", "🍋", "🔔", "💎", "7️⃣"]

# Payouts
payouts = {
    "🍒": 5,
    "🍋": 10,
    "🔔": 15,
    "💎": 20,
    "7️⃣": 50
}

def spin_reels():
    return [random.choice(symbols) for _ in range(3)]

def check_win(reels):
    if reels[0] == reels[1] == reels[2]:
        return payouts[reels[0]]
    return 0

def main():
    balance = 100
    bet_amount = 10

    print("Welcome to the Python Slot Machine!")
    print(f"You have ${balance}.\n")

    while balance >= bet_amount:
        input("Press Enter to spin...")

        reels = spin_reels()
        print(" | ".join(reels))

        winnings = check_win(reels)
        if winnings > 0:
            print(f"You won ${winnings} :DDDD!")
            balance += winnings
        else:
            print("No match, better luck next time D: !")
            balance -= bet_amount

        print(f"Current balance: ${balance}\n")

        if balance < bet_amount:
            print("Not enough funds to keep playing. Game over. xwx")
            break

        keep_playing = input("Play again? (y/n): ").strip().lower()
        if keep_playing != 'y':
            print("Thanks for playing :D!")
            break

if __name__ == "__main__":
    main()