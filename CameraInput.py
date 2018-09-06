import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, img = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #blur = cv2.medianBlur(gray, 5)

    #hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #edges = cv2.Canny(hsv, 40, 50)

    #cv2.imshow('edges',edges)
    #cv2.imshow('blur',blur)
    #cv2.imshow('gray',gray)
    cv2.imshow('cam',img)

    # img[:, :, 2] = 0
    # img[:, :, 0] = 0
    #thing, thresh1= cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    #thresh2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    #cv2.imshow('thresh1', thresh1)
    #cv2.imshow('thresh2', thresh2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()