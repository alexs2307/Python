import random
pc_choice = random.choice(["scissors","rock","paper"])

user_choice = input("What you choose - rock,paper or scissors?\n")
if pc_choice == user_choise:
    print("Repeat Again")
elif user_choice == "rock" and pc_choice == "scissors":
    print("You Win")
elif user_choice == "paper" and pc_choice == "rock":
    print("You Win")
elif user_choice == "scissors" and pc_choice == "paper":
    print("You Win")

else:
    print("You loose :( Pc Wins")