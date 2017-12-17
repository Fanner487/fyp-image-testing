import picamera
import threading
import time
from processing.qr import get_qr_code
from processing.scan import scan_image


def extract_code(file):
    """thread worker function"""
    # time.sleep(0.5)
    print 'Thread for: ' + file

    scan_image(file)
    
    # print image
    return




camera = picamera.PiCamera()


images = ["cam1", "cam2", "cam3", "cam4"]


for image in images:

	extract_code(image)

# while True:

# 	time.sleep(1)

# 	time_epoch = str(int(time.time()))
# 	image_path = "images/" + time_epoch + ".jpg"

# 	print "Taking photo: " + str(image_path)

# 	camera.capture(image_path)

# 	t = threading.Thread(target=extract_code, args=[time_epoch])
# 	t.start()

