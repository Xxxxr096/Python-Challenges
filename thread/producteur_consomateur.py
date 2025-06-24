import threading
import queue
import time


q = queue.Queue()


def producteur():
    for i in range(5):
        print(f"Producteur produit : {i}")
        q.put(i)
        time.sleep(1)


def consomateur():
    while True:
        item = q.get()
        print(f"Consommateur consomme {item}")
        q.task_done()


producteur_th = threading.Thread(target=producteur)
consomateur_th = threading.Thread(target=consomateur, daemon=True)

producteur_th.start()
consomateur_th.start()

producteur_th.join()
q.join()
