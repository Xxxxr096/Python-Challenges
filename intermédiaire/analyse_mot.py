from collections import Counter


def count_lettre(mot):
    i = 0
    for l in mot:
        if l != " ":
            i = i + 1
    return i


def count_phrase(phrase):
    i = 0
    for l in phrase:
        if l == ".":
            i += 1
    return i


def most_frequent_word(text):
    mots = text.split()
    compteur = Counter(mots)
    mot_plus_frequent, frequence = compteur.most_common(1)[0]
    return mot_plus_frequent, frequence


if __name__ == "__main__":
    para = str(input("Entez votre paragraphe : "))
    print(
        f"Votre paragraphe contient {count_lettre(para)} mots et de {count_phrase(para)} phrase!, le mot le plus commun est : {most_frequent_word(para)}"
    )
