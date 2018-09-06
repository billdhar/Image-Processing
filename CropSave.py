import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

img = cv2.imread('image1.jpg')

crop = img[200:700, 700:1200]

cv2.imshow('image',crop)

cv2.imwrite('saved.jpg', crop)

cv2.waitKey(0)
cv2.destroyAllWindows()