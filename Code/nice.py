import cv2
from preprocessing import *
from recognition import *

def threshold(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
	gray = cv2.bitwise_not(gray)
	gray = cv2.medianBlur(gray, 3) #blurring helps with noisy data (COUGH webcams)
	inp_thresh, cool = cv2.threshold(gray, 0, 255,		#do some preprocessing
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	return inp_thresh, cool

img = cv2.imread('test3.jpg')

scale_percent = 60 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
input = cv2.resize(img, dim, interpolation = cv2.INTER_AREA) 

unskewed = unskew(inp_thresh)

cv2.imshow("dj", inp_thresh)
cv2.imshow("djd", unskewed)

contours = find_contours(unskewed)
contoured = unskewed.copy();
#contoured = np.zeros((unskewed.shape[0], unskewed.shape[1], 3))
cv2.drawContours(contoured,contours,-1,(255,255,0),3)

cv2.imshow("djdd", contoured)

cv2.waitKey(0)

cv2.destroyAllWindows()

