def convertisseur_degre_fahren(temp):
    f = (temp * 9 / 5) + 32
    return f


def convertisseur_fahren_degre(temp):
    c = (temp - 32) * 5 / 9
    return c


if __name__ == "__main__":
    run = True
    while run:
        a = str(
            input("Quel température souhaiter vous convertir (F->C)/(C->F) :")
        ).upper()
        if a == "F->C":
            temp = int(input("Entrer la Température Fahrenheit :"))
            print(f"le resultat est : {convertisseur_fahren_degre(temp)}")
        else:
            temp = int(input("Entrer la Température Celsus :"))
            print(f"Le resultat est : {convertisseur_degre_fahren(temp)}")

        b = str(input("Voulez vous essayez une autre fois (oui/non): ")).lower()
        if b != "oui":
            print("Merci !")
            run = False
