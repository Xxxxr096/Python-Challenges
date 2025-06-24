import threading
import time

stock = []
lock = threading.Lock()
stop = threading.Event()  # Arreter un evenement


def producteur():
    for i in range(5):
        with lock:
            print(f"Le producteur a produit : {i}")
            stock.append(i)
        time.sleep(1)
    stop.set()  # dire au consomateur qu'on a finit


def consommateur():
    while not stop.is_set() or stock:
        with lock:
            if stock:
                item = stock.pop(0)
                print(f"consommateur a consommer {item}")
        time.sleep(1)


# Threads
t1 = threading.Thread(target=producteur)
t2 = threading.Thread(target=consommateur)

# Lancer les threads
t1.start()
t2.start()

# Attendre la fin
t1.join()
t2.join()

print("Tous les éléments ont été produits et consommés.")
