import os
from time import sleep

def get_qr_code(image_name):

	scans_dir = "scans/"
	codes_dir = "codes/"

	input_scan_path = scans_dir + image_name + "-result.png"
	output_qr_path = codes_dir + image_name + "-result.txt"

	if not os.path.exists(codes_dir):
		os.makedirs(codes_dir)

	os.system("zbarimg -q " + input_scan_path + " > " + output_qr_path)

	if os.path.exists(output_qr_path):


		strqrcode = open(output_qr_path, 'r').read()

		# print strqrcode
		print "Results for " + image_name + ": " + strqrcode

	else:
		print "QR-Code text file not found"

