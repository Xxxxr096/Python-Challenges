def voyelle(mot):
    list_voyelle = ["a", "e", "i", "o", "u", "y"]
    for let in mot:
        if let in list_voyelle:
            return True
    return False


if __name__ == "__main__":
    mot = str(input("Entrez le mot a vérifier : "))
    print(f"Le mot {"contient une voyelle !" if voyelle(mot) else "ne contient pas de voyelle !"}")