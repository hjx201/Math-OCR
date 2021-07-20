from PIL import Image
import pytesseract

try:
	img = Image.open('teehee.jpg') 
	pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
	text = pytesseract.image_to_string('teehee.jpg')
	print(text)