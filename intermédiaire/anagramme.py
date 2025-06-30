def detect_anagramme(mot1, mot2):

    mot1 = mot1.replace(" ", "").lower()
    mot2 = mot2.replace(" ", "").lower()
    if mot1 == mot2:
        print("❌ Les deux mots sont les meme !, donc pas de vrai anagramme. ")
    elif sorted(mot1) == sorted(mot2):
        print(f"✅ Les mots '{mot1}' et '{mot2}' sont des anagrammes.")
    else:
        print(f"❌ Les mots '{mot1}' et '{mot2}' ne sont pas des anagrammes.")


if __name__ == "__main__":
    mot1 = input("Entrez le premier mot : ")
    mot2 = input("Entrez le deuxième mot : ")
    detect_anagramme(mot1, mot2)
