import threading


def get_thread_name():
    print(f"je suis le thread : {threading.current_thread().name}")


thread1 = threading.Thread(target=get_thread_name, name="Poison")
thread2 = threading.Thread(target=get_thread_name, name="Virus")
thread3 = threading.Thread(target=get_thread_name, name="Banane")

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
