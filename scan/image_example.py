import picamera
import time

camera = picamera.PiCamera()


print(int(time.time()))

while True:

	time.sleep(1)

	image_path = "images/" + str(int(time.time())) + ".jpg"

	print "Taking photo: " + str(image_path)

	camera.capture(image_path)

