import random


def game():
    my_dict = {
        "rock": "🪨",
        "paper": "📄",
        "scissors": "✂️",
    }

    while True:
        joueur = input("Voulez vous jouer avec une IA ? (oui/non)").lower()
        if joueur == "non":
            joueur1 = input(
                "Joueur 1, choisissez votre position (rock/paper/scissors) : "
            )
            joueur2 = input(
                "Joueur 2, choisissez votre position (rock/paper/scissors) : "
            )
        else:
            joueur1 = input(
                "Joueur 1, choisissez votre position (rock/paper/scissors) : "
            )
            choix = ["paper", "rock", "scissors"]
            joueur2 = random.choice(choix)

        print(f"Joueur 1 : {my_dict.get(joueur1, '?')}")
        print(f"Joueur 2 : {my_dict.get(joueur2, '?')}")

        win = victory(joueur1, joueur2)

        if win == 1:
            print("Joueur 1 félicitations, vous gagnez !")
            break
        elif win == 2:
            print("Joueur 2 félicitations, vous gagnez !")
            break
        else:
            print("ÉGALITÉ ! Rejouez.\n")


def victory(joueur1, joueur2):
    victory_dict = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock",
    }

    if joueur1 == joueur2:
        return 0
    elif victory_dict[joueur1] == joueur2:
        return 1
    else:
        return 2


if __name__ == "__main__":
    game()
