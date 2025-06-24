import threading
import time

resultat = []
resultat_lock = threading.Lock()


def download(name, nb_fichier):

    for j in range(nb_fichier):
        i = 0
        while i < 100:
            time.sleep(5)
            i += 25
            print(f"Le thread {name} télecharge le fichier{j} : {i} % ")

        with resultat_lock:
            resultat.append((name, j))

    print(f"[{name}] Tous les fichiers ont été téléchargés.")


thread1 = threading.Thread(target=download, args=("choco", 5))
thread2 = threading.Thread(target=download, args=("banane", 5))
thread3 = threading.Thread(target=download, args=("caramello", 5))
thread4 = threading.Thread(target=download, args=("orange", 5))
thread5 = threading.Thread(target=download, args=("poiro", 5))


thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
print("\n✅ Téléchargements terminés. Résumé :")
for item in resultat:
    print(f" - {item[0]} a terminé le fichier {item[1]}")
