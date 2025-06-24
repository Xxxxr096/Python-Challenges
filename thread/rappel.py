import threading
from threading import Timer
import time

stop = threading.Event()


def rappel(nom):
    if not stop.is_set():
        print(f"Cela est un rappel du threading {nom} : soiyez courageux")
        t = Timer(3, rappel, args=("Blaize",))
        t.start()


def stop_rappel():
    print(f"Arret de l'appel effectuée.")
    stop.set()


if __name__ == "__main__":
    rappel("Blaizer")
    choice = input("Voulez vous arreter le rapelle ou pas? : ")
    if choice.lower() == "oui":
        thread = threading.Thread(target=stop_rappel)
        thread.start()
        thread.join()
    else:
        print(f"Le rappel continu alors.")
