import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

img = cv2.imread('image2.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(gray[500, 700])

cv2.imshow('gray', gray)
cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()