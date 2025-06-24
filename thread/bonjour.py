import threading
import time


def dire_bonjour():
    for i in range(5):
        print("Bonjour")
        time.sleep(3)


def dire_salut():
    for i in range(5):
        print("salut")
        time.sleep(3)


thread1 = threading.Thread(target=dire_bonjour)
thread2 = threading.Thread(target=dire_salut)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Programme fini")
