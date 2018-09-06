import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

img = cv2.imread('image3.jpg')

print(img[140][240])

cv2.imshow('image',img)

img = mpimg.imread('image3.jpg')
print(img[140][240])
plt.imshow(img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()