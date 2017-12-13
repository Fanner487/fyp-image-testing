import threading
import time

def worker(image):
    """thread worker function"""
    # time.sleep(0.5)
    print '\nWorker' + image
    # print image
    return

images = ['phone1.jpg', 'phone2.jpg', 'phone2.jpg']
threads = []

for image in images:
    t = threading.Thread(target=worker, args=[image])
    threads.append(t)

    t.start()