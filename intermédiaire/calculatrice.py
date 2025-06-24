def multiplication(a, b):
    return a * b


def soustraction(a, b):
    return a - b


def addition(a, b):
    return a + b


def division(a, b):
    try:
        if b != 0:
            return a / b
        else:
            return "Erreur : division par zéro."
    except Exception as e:
        return f"Une erreur s'est produite : {e}"


if __name__ == "__main__":
    print("Bienvenu dans ma Calculatrice")
    run = True
    while run:
        a = int(input("choisisez a : "))
        b = int(input("choisisez b : "))
        choice = str(
            input(
                """Que souhaite tu calculer
                    - +
                    - _
                    - /
                    - * : 
                    
                    """
            )
        ).lower()
        match choice:
            case "+":
                print(f"Le resultat de l'addition est {addition(a,b)}")
            case "-":
                print(f"Le résultat de la soustraction est = {soustraction(a,b)}")

            case "*":
                print(f"Le résultat de la multiplication est = {multiplication(a,b)}")
            case "/":
                print("faite attention de fournir un b !=0")
                print(f"Le résultat de la division est = {division(a,b)}")
            case _:
                print("Option inconnue.")
        choice_stay = str(input("Souhaitez vous faire une autre opération ?")).lower()
        if choice_stay != "oui":
            print("A bientot!")
            run = False
