import cv2
import numpy as np


img = cv2.imread('image2.jpg')
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#blur = cv2.bilateralFilter(img,9,75,75)
#blur = cv2.GaussianBlur(img,(5,5),0)
blur = cv2.medianBlur(img,5)

# hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

# edges = cv2.Canny(hsv, 1, 50)

# cv2.imshow('Edges',edges)

cv2.imshow('Screenshot',blur)
cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

