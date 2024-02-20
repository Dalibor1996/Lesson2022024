import threading
import time

def background_task():
    while True:
        print("Deamon thread is running...")
        time.sleep(2)


daemon_thread = threading.Thread(target=background_task, args=(), daemon=True)
daemon_thread.start()

print("Zacni program")
time.sleep(20)
print("Ukonci program")
