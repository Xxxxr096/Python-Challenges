def verify(a):
    if a % 2 == 0:
        return "pair"
    return "impaire"


if __name__ == "__main__":
    a = int(input("Entrez le nombre que vous voulez vérifier: "))
    print(f"Le nombre choisie est : {verify(a)}")
