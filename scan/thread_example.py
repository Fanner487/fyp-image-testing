import threading
import time
from qr import get_qr_code
from scan import scan_image

def worker(file):
    """thread worker function"""
    # time.sleep(0.5)
    print '\nWorker' + image

    scan_image(file)
    get_qr_code(file + "-result.png")
    # print image
    return

images = ['phone1', 'phone2', 'phone3']
threads = []

for image in images:
    t = threading.Thread(target=worker, args=[image])
    threads.append(t)

    t.start()