import random

public_choice = input("Select your PM: Imran Khan or Nawaz Sharif: ")

if public_choice.lower() not in ["imran khan", "nawaz sharif"]:
    print("Invalid input")
else:
    select = random.choice(["nawaz sharif"])

    print("You chose:", public_choice)
    print("Random choice:", select)

    if public_choice.lower() == select.lower():
        print("You won!")
    else:
        print("You lost!")
