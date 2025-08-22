import random


def rendom_ia():
    a = random.randint(1, 100)
    return a


def main():
    a = int(input("choisisez une nombre entre 1-100 : "))
    ia = rendom_ia()
    if a > ia:
        print("Le nombre choisie est supérieur a celui de l'ordinateur")
        print(f"Le nombre choisie par l'ordinateur est : {ia}")
    elif a < ia:
        print("le nombre choisie est inférieur a celui de l'ordinateur")
        print(f"Le nombre choisie par l'ordinateur est : {ia}")
    else:
        print("Bravo ! vous avez trés bien deviner le nombre")
    choix = input("Voulez vous refaire ou continuer refaire/quiter : ").lower()
    if choix == "refaire":
        main()
    else:
        print("Merci de participer ! ")


if __name__ == "__main__":
    main()
