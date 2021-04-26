import random


def roll_dice():
    dice_total = random.randint(1, 6) + random.randint(1, 6)
    return dice_total

def main():
    player1 = input("Player 1 name\n")
    print(player1.upper())
    player2 = input("Player 2 name\n")
    print(player2.upper())

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1.upper(), "rolled", roll1)
    print(player2.upper(), "rolled", roll2)

    if roll1 > roll2:
        print(player1.upper(), "wins")
    elif roll1 == roll2:
        print("Draw")
    else:
        print(player2.upper(), "wins")
main()