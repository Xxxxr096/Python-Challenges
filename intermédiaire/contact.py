import json
import os


def load_json(data):
    with open("contact.json", "w") as fichier:
        json.dump(data, fichier, indent=4)


def afficher():
    if os.path.exists("contact.json"):
        with open("contact.json", "r") as fichier:
            data = json.load(fichier)
            return data
    else:
        return []


def ajouter_contact():
    nom = input("Nom : ")
    tel = input("Téléphone : ")
    email = input("Email : ")

    contact = {"nom": nom, "telephone": tel, "email": email}

    contacts = afficher()
    contacts.append(contact)
    load_json(contacts)
    print("✅ Contact ajouté avec succès.")


def afficher_contacts():
    contacts = afficher()
    if contacts:
        print("📋 Liste des contacts :")
        for c in contacts:
            print(f"- {c['nom']} | 📞 {c['telephone']} | ✉️ {c['email']}")
    else:
        print("📭 Aucun contact enregistré.")


# Menu principal
if __name__ == "__main__":
    while True:
        print("\n--- MENU CONTACT ---")
        print("1. Ajouter un contact")
        print("2. Afficher les contacts")
        print("3. Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            ajouter_contact()
        elif choix == "2":
            afficher_contacts()
        elif choix == "3":
            print("👋 Au revoir !")
            break
        else:
            print("❌ Option invalide. Réessayez.")
