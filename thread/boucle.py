import threading


lock = threading.Lock()
resultat = []


def loop(nom):

    compteur = 0
    for i in range(1000):
        with lock:
            compteur += 1
    print(f"Le thread {nom} a finit avec {compteur}")
    resultat.append((nom, compteur))


thread1 = threading.Thread(target=loop, args=("thread1",))
thread2 = threading.Thread(target=loop, args=("thread2",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
