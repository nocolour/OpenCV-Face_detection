import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(3,320) # set Width (640)
cap.set(4,240) # set Height (480)

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1) # or -1
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,     
        scaleFactor=1.1, # 1.2
        minNeighbors=7,  # 5   
        minSize=(30, 30)  # (20,20)
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]  
    cv2.imshow('video',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        breakcap.release()
cv2.destroyAllWindows()