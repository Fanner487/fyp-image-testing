import os
from time import sleep

def get_qr_code(image_name):

	input_scan_path = "scans/" + image_name + "-result.png"
	output_qr_path = "codes/" + image_name + "-result.txt"

	os.system("zbarimg -q " + image_name + " > " + output_qr_path)

	if os.path.exists(output_qr_path):


		strqrcode = open(output_qr_path, 'r').read()

		# print strqrcode
		print "Results for " + image_name + ": " + strqrcode

	else:
		print "QR-Code text file not found"

