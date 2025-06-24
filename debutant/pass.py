import random

import secrets
import string


def generer_mot_de_passe(taille=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = "".join(secrets.choice(caracteres) for _ in range(taille))
    return mot_de_passe


taille = int(input("Entrez la taille du mot de passe souhaitée : "))
print("🔐 Mot de passe généré :", generer_mot_de_passe(taille))
