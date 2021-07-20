#import shiz

import cv2
import time

from preprocessing import *
from recognition import *
from solver import * 

#start video
print("[INFO] starting video stream...")
vs = cv2.VideoCapture(0)
time.sleep(1.0)

vs.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
vs.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

readrect = [200, 200, 500,300]
solnrect = [500,200, 600,300]

solution = "e"
shownsol = ""
# loop over frames from the video stream
while True:
	# grab the current frame, then handle if we are using a
	# VideoStream or VideoCapture object
	ret, frame = vs.read()
	# check to see if we have reached the end of the stream
	if frame is None:
		break
	# resize the frame, maintaining the aspect ratio
	orig = frame.copy()

	cv2.rectangle(orig, (readrect[0], readrect[1]), (readrect[2], readrect[3]), (0, 255, 0), 2)
	cv2.rectangle(orig, (solnrect[0], solnrect[1]), (solnrect[2], solnrect[3]), (255, 255, 0), 2)
	
	input = orig[readrect[1]:readrect[3], readrect[0]:readrect[2]] #get input that's inside the rectangle 
	
	#preprocess the image
	inp_thresh = threshold(input)
	unskewed = unskew(inp_thresh)
	
	contours = find_contours(unskewed)

	#contoured = draw_charboxes(unskewed.copy(), boxes)
	
	#symbols = get_symbol_imgs(unskewed, boxes)
	e = contours_to_text(contours, unskewed)
	print(e)
	
	solution = solve(e)
	if (solution != ""):
		shownsol = solution;
	
	output = orig.copy()
	
	cv2.putText(output, solution, (solnrect[0]+10, solnrect[1]+20),
		cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
	
	#show the results
	cv2.imshow("Homework Machine", output)# show the output frame
	
	cv2.imshow("unskewed", unskewed)
	
	
	key = cv2.waitKey(1) & 0xFF
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break	
	
# if we are using a webcam, release the pointer

vs.release()

# close all windows
cv2.destroyAllWindows()	