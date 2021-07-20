import os, os.path
import cv2
from PIL import Image
import glob
from preprocessing import *
from recognition import *

#code used to extract characters based on bounding boxes.

image_list = []

folder = ('output')

filenum = 0



for filename in glob.glob('testimgs//*.jpg'):
	input = cv2.imread(filename)
	
	cv2.imshow("loser", input)
	cv2.waitKey(0)
	
	inp_thresh = threshold(input)
	unskewed = unskew(inp_thresh)
	contours = find_contours(unskewed)
	boxes = get_charboxes(contours)
	symbols = get_symbol_imgs(unskewed, boxes)
	
	for sym in symbols:
		while(os.path.exists('output//' + str(filenum) + ".jpg")):
			filenum += 1
		cv2.imwrite(folder + '\\' + str(filenum) + '.jpg', sym)
		filenum += 1