import os
from time import sleep

def get_qr_code(image_name):

	images_dir = "images/"
	codes_dir = "codes/"

	input_scan_path = images_dir + image_name + "-result.png"
	output_qr_path = codes_dir + image_name + "-result.txt"

	if not os.path.exists(output_qr_path):
		os.makedirs(output_qr_path)

	os.system("zbarimg -q " + image_name + " > " + output_qr_path)

	if os.path.exists(output_qr_path):


		strqrcode = open(output_qr_path, 'r').read()

		# print strqrcode
		print "Results for " + image_name + ": " + strqrcode

	else:
		print "QR-Code text file not found"

