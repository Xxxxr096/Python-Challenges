def palindrome(mot):
    mot.lower().replace(" ", "")
    return mot == mot[::-1]


if __name__ == "__main__":
    mot = str(input("Entrez le mot à vérifier : "))
    print(f"Le mot {"nest pas palindrom" if palindrome(mot) == False else "est palindrome"}")