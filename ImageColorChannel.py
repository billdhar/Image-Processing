import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

img = cv2.imread('image.jpg')
img_org = cv2.imread('image.jpg')

#img[125:500,150:1000,0] = 0
img[:,:,0] = 0
img[:,:,1] = 0

plt.imshow(img)
plt.draw()

plt.figure()
plt.imshow(img_org)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()