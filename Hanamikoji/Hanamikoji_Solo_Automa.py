# Solo Automa mode for Hanamikoji
# author : Faruk
# Version : 1.0

import random

actions = ['Secret', 'Depot', 'Offre', 'Echange']


def pick_action():
    Hana_choice = random.choice(actions)
    actions.remove(Hana_choice)
    print(f"Hana : {Hana_choice}")
    print(f"Action left : {actions}")


def first_player():
    Hana_choice = random.choice(range(1, 50))
    if Hana_choice < 25:
        print("Hana first")
    else:
        print("You first")


game_over = False
while not game_over:
    choice = input("yes or no?:\n")
    if choice == "y":
        pick_action()
        if len(actions) < 1:
            print('No more action left for Hana')
            game_over = True

    else:
        game_over = True

