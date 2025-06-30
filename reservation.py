class Reservation:
    def __init__(self, prix):
        self.personne = []
        self.type_reservation = []
        self.prix = prix

    def get_nom(self, personne):
        return self.personne[personne.nom]

    def get_adress(self, personne):
        return self.personne[personne.adresse]

    def ajout_reservation(self, type):
        self.type_reservation.append(type)
        return self.type_reservation

    def reduction(self):
        if self.prix >= 500:
            print("Vous avez le droit a une réduction de 20%")
            self.prix = self.prix * 0.2
        else:
            print(
                f"Vous n'avez pas le droit a une réduction votre montant est inférieur a 500$"
            )
        return self.prix

    def ajout_person(self, pers):
        self.personne.append(pers)
        return self.personne

    def anul_reservation(self):
        choice = input(
            "voulez vous annulez la reservation pour tout le monde ? (oui/non) : "
        )
        if choice.lower() == "non":
            pers_to_delet = int(
                input(
                    "Quel personne voulez vous supprimer ? (entrez le numéro de la personne) : "
                )
            )
            for i, pers in enumerate(self.personne):
                print(f"{i+1} - {pers}")
            print(
                f"Vous avez choicies d'annuler la reservation de MR/Ms {self.personne[pers_to_delet -1]}"
            )
            del self.personne[pers_to_delet - 1]

        return self.personne

    def __str__(self):

        print(
            f"""Votre reservation est la suivante :
                - pers  : {[self.personne[i].nom for i in range(len(self.personne))]}
                - type reservation : {[i for i in self.type_reservation]}
                - prix total = {self.reduction()}
                """
        )


class Person:
    def __init__(self, nom, adresse, age):
        self.nom = nom
        self.adresse = adresse
        self.age = age

    def reserver(self):
        pass


class Majeur(Person):
    def __init__(self, nom, adresse, age):
        super().__init__(nom, adresse, age)
        self.type = "MA"


class Mineur(Person):
    def __init__(self, nom, adresse, age):
        super().__init__(nom, adresse, age)
        self.type = "MI"


class Ado(Person):
    def __init__(self, nom, adresse, age):
        super().__init__(nom, adresse, age)
        self.type = "ADO"


class Cinema:
    def __init__(self, nom_cinema, nom_film, heure, duree):
        self.nom_cinema = nom_cinema
        self.nom_film = nom_film
        self.heure = heure
        self.duree = duree

    def reservation_prix(self, personne):
        if self.nom_cinema == "Cinéma De Luxe de Paris":
            if personne.type == "MI":
                prix = 30 * 0.2
            else:
                prix = 30
        elif self.nom_cinema == "Cinéma De Barbés":
            if personne.type == "MI":
                prix = 8.99 * 0.2
            else:
                prix = 8.99
        elif self.nom_cinema == "Grand Charles Du pont":
            if personne.type == "MI":
                prix = 50 * 0.2
            else:
                prix = 50

        else:
            prix = 10

        return prix


if __name__ == "__main__":
    reservation = Reservation(0)
    print(
        f"Bienvenu dans Tout Reservable pour une meilleure réservation et plus complete"
    )
    while True:
        try:
            pers = int(input("Vous voulez reserver pour combien de personne ? : "))
            if pers < 0:
                print("Le nombre de personnes est incorrect")
                continue
            break
        except ValueError:
            print("Veuillez entrez un nombre valide")

    for i in range(pers):
        while True:
            try:
                age = int(input(f"Quel est l'âge de la personne {i + 1} : "))
                if age < 0:
                    print("L'âge ne peut pas être négatif.")
                    continue
                break
            except ValueError:
                print("Veuillez entrer un âge valide (nombre entier).")

        name = input(f"quel est le nom de la personne {i +1} : ")
        adress = input(f"quel est l'adress de la personne :  {i+1}")
        if age < 13:
            pers = Ado(name, adress, age)
        elif 13 <= age <= 17:
            pers = Mineur(name, adress, age)
        else:
            pers = Majeur(name, adress, age)
        reservation.ajout_person(pers)

    type_reservation = input("Que voulez vous reserver ? (Cinéma):")
    if type_reservation.lower() == "cinéma":
        reservation.ajout_reservation(type_reservation)
        nom_cinema = input("Quel est le cinema de votre choix :")
        nom_film = input("Quel film souhaitez vous regardez ?  : ")
        heure = input("A quel heure souhaitez vous regardez le filme : ")

        cinema_group = Cinema(nom_cinema, nom_film, heure, "2h")

        print("Calcule des prix veuillez patienter ......")
        somme = 0
        for i in reservation.personne:
            prix = cinema_group.reservation_prix(i)
            somme = somme + prix
        reservation.prix = somme
        prix_finale = reservation.reduction()

        print(
            f"Le prix de votre reservation aprés etude de vos droits de reduction pour le cinema de {nom_cinema} est de : {prix_finale} pour {len(reservation.personne)} personne."
        )
        print("Imprimation ticket...")
        reservation.__str__()

    print(f"Merci de bous avoir fait confiance")
