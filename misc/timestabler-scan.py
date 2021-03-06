#import packages.
from skimage.filters import threshold_local
import numpy as np 
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path of image")
args = vars(ap.parse_args())

print(args)

#load image


image = cv2.imread(args["image"])
ratio = image.shape[0] / 500.0
orig = image.copy()
image = imutils.resize(image, height = 500)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 75, 200)

print("Edge Detection yas")
cv2.imshow("Image", image)
cv2.imshow("Edged", edged)
cv2.waitKey(0)
