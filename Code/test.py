import cv2
import imutils
import numpy as np
import cv2

#takes a pre-cropped picture and extracts the equation from it to solve.
from solver import solve
from preprocessing import *
from recognition import *

import argparse

ap = argparse.ArgumentParser(description='takes in an image.')

ap.add_argument("-i", "--image", type=str,
	help="path to input image file")

args = vars(ap.parse_args())

#img = cv2.imread('test3.jpg')
img = cv2.imread(args["image"])

scale_percent = 60 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
input = cv2.resize(img, dim, interpolation = cv2.INTER_AREA) 

#preprocess the image
inp_thresh = threshold(input)
unskewed = unskew(inp_thresh)

contours = find_contours(unskewed)
unskewed = cv2.drawContours(unskewed, contours, 3, (0,255,0), 3)
boxes = get_charboxes(contours)
print(boxes)
contoured = draw_charboxes(unskewed.copy(), boxes)

cv2.imshow("Homework Machine", inp_thresh)# show the output frame

cv2.imshow("unskewed", contoured)

while True:
	key = cv2.waitKey(1) & 0xFF
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break;