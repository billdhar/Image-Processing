import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

img = cv2.imread('image2.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imshow('hsv', hsv)
cv2.imshow('rgb', rgb)
cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()