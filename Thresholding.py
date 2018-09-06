import cv2
import numpy as np

img = cv2.imread('image3.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thing, thresh1= cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
thresh2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('threahold1', thresh1)
cv2.imshow('threshold2', thresh2)

cv2.waitKey(0)
cv2.destroyAllWindows()