class Client:
    def __init__(self, nom, rang, arrivee):
        self.nom = nom
        self.rang = rang
        self.arrivee = arrivee  # numéro d’arrivée

    def affiche_client(self):
        print(f"Client {self.nom} - Priorité: {self.rang} - Arrivée: {self.arrivee}")


class Banque:
    def __init__(self):
        self.lst_client = []
        self.compteur = 0

    def ajout_client(self, nom, rang):
        self.compteur += 1
        client = Client(nom, rang, self.compteur)
        self.lst_client.append(client)

    def afficher_file(self):
        for client in self.get_clients_ordonnes():
            client.affiche_client()

    def get_clients_ordonnes(self):
        priorite = {"VIP": 0, "senior": 1, "normal": 2}
        return sorted(self.lst_client, key=lambda c: (priorite[c.rang], c.arrivee))

    def servir_client(self):
        if not self.lst_client:
            print("Aucun client à servir.")
            return
        client_serve = self.get_clients_ordonnes()[0]
        self.lst_client.remove(client_serve)
        print(f"Client servi : {client_serve.nom} ({client_serve.rang})")


if __name__ == "__main__":

    banque = Banque()
    banque.ajout_client("Émilie", "normal")
    banque.ajout_client("François", "senior")
    banque.ajout_client("Giselle", "VIP")
    banque.ajout_client("Henri", "senior")
    banque.ajout_client("Inès", "VIP")
    banque.ajout_client("Julien", "normal")

    print("📋 File actuelle :")
    banque.afficher_file()

    print("\n👨‍💼 Service en cours :")
    banque.servir_client()

    print("\n📋 File après service :")
    banque.afficher_file()
