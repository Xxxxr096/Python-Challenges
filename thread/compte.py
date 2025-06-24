import time
import threading


def compter():
    i = 0
    while True:
        print(f"Temps écoulé : {i} secondes")
        i += 1
        time.sleep(1)


if __name__ == "__main__":
    # Créer et démarrer le thread
    thread1 = threading.Thread(target=compter, daemon=True)
    thread1.start()

    # Attendre une entrée de l'utilisateur
    input("Appuyez sur Entrée pour arrêter le chrono...\n")

    print("Vous avez arrêté le chronomètre.")
