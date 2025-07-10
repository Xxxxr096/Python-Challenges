import json


def load_json():
    try:
        with open("data.json", "r") as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        print("Le fichier n'exsite pas. Créaation en cour")
        return []


def main():
    while True:
        options = [
            "Ajouter une tache",
            "supprimer une tache",
            "modifier une tache",
            "Quiter",
        ]
        print("==== Liste Des Option ====")
        for i, option in enumerate(options, 1):
            print(f"{i} - {option}")

        choix = int(input("Choisisez une option : "))
        if choix == 1:
            tache = input("Entrez votre tache")
            data = load_json()
            data.append(tache)
            with open("data.json", "w") as fichier:
                json.dump(data, fichier, indent=4, ensure_ascii=False)
                print("Tache sauvegarder")
        elif choix == 2:
            tache = input("Quel tache souhaitez vous supprimer : ")
            data = load_json()
            try:
                if tache in data:
                    data.remove(tache)
                    print("Tache supprimer avec succées")
                with open("data.json", "w") as fichier:
                    json.dump(data, fichier, indent=4, ensure_ascii=False)
                    print("Base de donnée a jour !")
            except:
                print("Tache non trouver")
        elif choix == 3:
            try:
                data = load_json()
                tache = input("Qeul tache souhaitez vous modifier ? :  ")
                if tache in data:
                    tache_modif = input("Modifier votre Tache : ")
                    index = data.index(tache)
                    data[index] = tache_modif
                    print("Tache Modifier !")
                with open("data.json", "w") as fichier:
                    json.dump(data, fichier, indent=4, ensure_ascii=False)
                    print("Base de donnée a jour !")

            except:
                print("La Tache n'est pas disponible")
        else:
            print("A Bientot")
            break


if __name__ == "__main__":
    main()
