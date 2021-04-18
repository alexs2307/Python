from random import randint
secret_number = randint(1, 30)
guess = 0
while guess != secret_number:
    number = input("Guess the secret number \n")
    guess = int(number)
    if guess == secret_number:
        print("You win")
    else:
        if guess > secret_number:
            print("Too high try something smaller")
        else:
            print("Too low try something bigger")
print("Game over")