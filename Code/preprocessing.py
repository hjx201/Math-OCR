import numpy as np
import cv2

def threshold(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
	gray = cv2.bitwise_not(gray)
	gray = cv2.medianBlur(gray, 3) #blurring helps with noisy data (COUGH webcams)
	inp_thresh = cv2.threshold(gray, 0, 255,		#do some preprocessing
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	return inp_thresh
	

def unskew(img):
	#because tesseract is bad at reading rotated stuff
	
	#find the text (assumes white on black background, and already thresholded image)
	coords = np.column_stack(np.where(img > 0))
	angle = cv2.minAreaRect(coords)[-1]

# the `cv2.minAreaRect` function returns values in the
# range [-90, 0); as the rectangle rotates clockwise the
# returned angle trends to 0 -- in this special case we
# need to add 90 degrees to the angle
	if angle < -45:
		angle = -(90 + angle)
# otherwise, just take the inverse of the angle to make
# it positive
	else:
		angle = -angle

# rotate the image to deskew it
	(h, w) = img.shape[:2]
	center = (w // 2, h // 2)
	M = cv2.getRotationMatrix2D(center, angle, 1.0)
	unskewed = cv2.warpAffine(img, M, (w, h),
	flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
	
# draw the correction angle on the image so we can validate it
	#cv2.putText(unskewed, "Angle: {:.2f} degrees".format(angle),
		#(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
		
	return unskewed