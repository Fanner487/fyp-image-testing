import threading
import time

def worker():
    """thread worker function"""
    # time.sleep(0.5)
    print '\nWorker'
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)

    t.start()