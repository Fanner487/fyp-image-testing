import os
from time import sleep

def get_qr_code(image_path):

	output_qr_path = image_path + "-result.txt"

	os.system("zbarimg -q " + image_path + " > " + output_qr_path)

	if os.path.exists(output_qr_path):


		strqrcode = open(output_qr_path, 'r').read()

		# print strqrcode
		print "Results for " + image_path + ": " + strqrcode

	else:
		print "QR-Code text file not found"

