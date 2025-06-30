def main():
    lst_mot = ["pomme", "chevale", "escalope", "chat", "frommage", "oeuf"]
    print("Bonjour on va commencer la Partie, Bon jeux !.")
    for mot in lst_mot:
        l = len(mot)
        erreur = 0
        chaine = ["-" for _ in range(l)]
        print("Mot à deviner :", "".join(chaine))
        while erreur < 7 and "-" in chaine:
            lettre = input("Entrez la lettre deviner :")
            if lettre in mot:
                for i in range(len(mot)):
                    if mot[i] == lettre:
                        chaine[i] = lettre
                print("Mot :", "".join(chaine))
            else:
                erreur += 1
                print(
                    f"Faux tentez une autre fois, Attention il vous reste {7 - erreur} essaye"
                )

        if "-" not in chaine:
            print("Bravo vous avez gagnez !.")
        else:
            print(f"Dommage, vous avez perdu ! Le mot était : {mot}")


if __name__ == "__main__":
    main()
