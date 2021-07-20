import cv2

from preprocessing import *
from recognition import *
from solver import * 
from east import *

input = cv2.imread('test4.jpg')

boxes = east(input, .2)

output = input.copy()
	
# initialize the list of results
results = []
# loop over the bounding boxes
for (startX, startY, endX, endY) in boxes:
	cv2.rectangle(output, (startX, startY), (endX, endY),
		(0, 0, 255), 2)
	roi = input[startY:endY, startX:endX]
		#preprocess the image
	inp_thresh = threshold(roi)
	unskewed = unskew(inp_thresh)
	contours = find_contours(unskewed)
	
	str = contours_to_text(contours, unskewed)
	print(str)
	text = solve(str)
	
	print(text)
	
	# add the bounding box coordinates and OCR'd text to the list
	# of results
	results.append(((startX, startY, endX, endY), text))
	
	
cv2.imshow("output", output)
cv2.waitKey(0)

cv2.destroyAllWindows()
	
