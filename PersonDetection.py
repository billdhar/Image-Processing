import numpy as np
import cv2

full_body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
upper_body_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')
lower_body_cascade = cv2.CascadeClassifier('haarcascade_lowerbody.xml')

fourcc = cv2.VideoWriter_fourcc(*'MP42')

cap = cv2.VideoCapture('Test 2.mp4')
out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (1280,720))

while(True):


    ret, img = cap.read()

    if ret:

        #img = cv2.rotate(img, cv2.ml.ROW_SAMPLE, cv2.ROTATE_90_CLOCKWISE)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detects faces of different sizes in the input image
        body = full_body_cascade.detectMultiScale(gray, 1.2, 5)

        for (x, y, w, h) in body:
            # To draw a rectangle in a face
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

        # Detects faces of different sizes in the input image
        upper_body = upper_body_cascade.detectMultiScale(gray, 1.2, 5)

        for (x, y, w, h) in upper_body:
            # To draw a rectangle in a face
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

        # Detects faces of different sizes in the input image
        lower_body = lower_body_cascade.detectMultiScale(gray, 1.2, 5)

        for (x, y, w, h) in lower_body:
            # To draw a rectangle in a face
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

        # Display an image in a window
        cv2.imshow('img', img)

        out.write(img)

        # Wait for Esc key to stop
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break

out.release()
# Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()
