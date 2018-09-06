import cv2
import numpy as np


img = cv2.imread('image1.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

edges = cv2.Canny(hsv, 100, 200)
# kernel = np.ones((5,5),np.uint8)
# dilation = cv2.dilate(edges,kernel,iterations = 10)
# closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)

# res = cv2.bitwise_and(img, img, mask= edges)

cv2.imshow('Edges',edges)

cv2.imshow('Screenshot',img)

cv2.waitKey(0)
cv2.destroyAllWindows()