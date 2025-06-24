import random


def nombre_myster(your_number):
    random_number = random.randint(1, 100)
    if random_number == your_number:
        print(f"Vous avez devinez le nombre correct qui est {random_number}")
    else:
        print(
            f"Vous avez devinez le mauvais nombre. Le nombre mystére est : {random_number}"
        )


if __name__ == "__main__":
    run = True
    while run:
        try:
            your_number = int(input("🔢 Devinez le nombre entre 1 et 100 : "))
            if not 1 <= your_number <= 100:
                print("⚠️ Veuillez entrer un nombre entre 1 et 100.")
                continue
        except ValueError:
            print("⚠️ Veuillez entrer un nombre valide.")
            continue

        nombre_myster(your_number)

        retry = input("🔁 Voulez-vous réessayer votre chance ? (oui/non) : ").lower()
        if retry != "oui":
            print("👋 Merci pour votre participation !")
            run = False
