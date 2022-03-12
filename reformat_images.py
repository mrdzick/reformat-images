import sys
import os
from PIL import Image


def scan_directory(directory):
	""" This function will scan the directory and return the list of files inside of it"""
	for root, dirs, files in os.walk(directory, topdown=False):
		# files variable will not contain the hidden files
		files = [f for f in files if not f[0] == '.']
	return files

def reformat_images(src_directory, dst_directory):
	"""This function will rotate image, resize it, and save it as .jpeg in dst_directory"""
	files = scan_directory(src_directory)

	for file in files:
		#get path of each file
		file_path = src_directory + '/' + file

		#open each file
		with Image.open(file_path) as img:
			#rotate each image
			img = img.rotate(90)
			#resize each image
			img = img.resize((128, 128))
			#generate the jpeg image in dst_directory
			print('Generating: {}.jpg'.format(file))
			img.convert('RGB').save(dst_directory + file + '.jpg')



if __name__ == '__main__':
	src_directory = sys.argv[1]
	dst_directory = sys.argv[2]
	reformat_images(src_directory, dst_directory)
