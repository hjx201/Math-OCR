import pytesseract
import cv2

def find_contours(img):
	contours = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
	
	contours = contours[0]
	
	return contours

def get_charboxes(contours): #get bounding boxes w/o an input
	bounds = []
	for i in range(len(contours)):
		if cv2.contourArea(contours[i]) > 200:
			bound = cv2.boundingRect(contours[i])
			bounds.append(bound)
		
	bounds_cut = []
	isBottomEquals = False;
	nextIsBottomEquals = False;
	for i in range(len(bounds)):
		(x1, y1, w1, h1) = bounds[i]
		
		#find equals sign
		if (i+1 < len(bounds)):
			
			(x2, y2, w2, h2) = bounds[i+1]
	
			if(abs(x1-x2)<20):
				nextIsBottomEquals = True;
				minX = min(x1, x2)
				minY = min(y1, y2)
				maxX = max(x1+w1, x2+w2)
				maxY = max(y1+h1, y2+h2)
			
				x1 = minX
				y1 = minY
				w1 = maxX-minX
				h1 = maxY-minY
		
		if(isBottomEquals == False):
			bounds_cut.append((x1, y1, w1, h1))
		else:
			isBottomEquals = False;
		
		if (nextIsBottomEquals):
			isBottomEquals = True;
			nextIsBottomEquals = False;

	bounds_cut.sort(key=lambda x:x[0])
	return bounds_cut
	
def contours_to_text(contours, img):
	outputstr = ""
	
	bounds = []
	for i in range(len(contours)):
		if cv2.contourArea(contours[i]) > 200:
			bound = cv2.boundingRect(contours[i])
			bounds.append(bound)
		
	bounds.sort(key=lambda x:x[0])
	print(bounds)
	
	isBottomEquals = False;
	nextIsBottomEquals = False;
	isDash = False;
	for i in range(len(bounds)):
		(x1, y1, w1, h1) = bounds[i]
		
		#find equals sign
		if (i+1 < len(bounds)):
			
			(x2, y2, w2, h2) = bounds[i+1]
	
			if(abs(x1-x2)<20):
				nextIsBottomEquals = True;
				minX = min(x1, x2)
				minY = min(y1, y2)
				maxX = max(x1+w1, x2+w2)
				maxY = max(y1+h1, y2+h2)
			
				x1 = minX
				y1 = minY
				w1 = maxX-minX
				h1 = maxY-minY
			elif(w1/h1 > 3 and isBottomEquals == False):
				isDash = True
			
		if(isBottomEquals):
			isBottomEquals = False;
		elif(nextIsBottomEquals):
			outputstr += "="
			isBottomEquals = True;
			nextIsBottomEquals = False;
		elif(isDash):
			outputstr += "-"
			isDash = False;
		else:
			box = bounds[i] #get the rectangle
			tessimg = img[box[1]:box[1]+box[3], box[0]:box[0]+box[2]]
			outputstr += pytesseract.image_to_string(tessimg, config='-l mat --psm 10')
	
	return outputstr


def get_symbol_imgs(img, boxes):
	symbolimgs = []
	for box in boxes:
		symbolimgs.append(img[box[1]:box[1]+box[3], box[0]:box[0]+box[2]])
	return symbolimgs
	
def draw_charboxes(img, bounds):
	output = img.copy()
	
	for bound in bounds:
		
		(x, y, w, h) = bound
		cv2.rectangle(output, (x, y), (x + w, y + h), (70,0,70), 3)
		
	return output
	