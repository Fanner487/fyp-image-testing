import os
from time import sleep

# countdown = 3

# output_image_path = "scan.png"
# # output_qr_path = "result.txt"
def get_qr_code(image_path):

	output_qr_path = image_path + "-result.txt"

	os.system("zbarimg -q " + image_path + " > " + output_qr_path)

	if os.path.exists(output_qr_path):

		strqrcode = open(output_qr_path, 'r').read()

		print strqrcode

	else:
		print "QR-Code text file not found"

