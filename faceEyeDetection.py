'''
Haar Cascade Face and Eye detection with OpenCV
	Based on tutorial by pythonprogramming.net
    Visit original post: https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/
Adapted by Marcelo Rovai - MJRoBot.org @ 22Feb2018
'''

import cv2

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
faceCascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
cap.set(4, 640)  # set Width (640)
cap.set(3, 480)  # set Height (480)

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,  # (1.3)
        minNeighbors=5,  # (5)
        minSize=(25, 25)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        eyes = eyeCascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.2,  # (1.5)
            minNeighbors=7,  # (7)
            minSize=(3, 3),  # (5, 5)
        )

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        cv2.imshow('video', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:  # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()