#!/usr/bin/python36
# coding: utf-8
# Press Enter key to Exit.


import cv2



cap = cv2.VideoCapture(0)
while True:
    ret, photo = cap.read()
    fd = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    coords = fd.detectMultiScale(photo)
    final_photo = photo
    if len(coords) == 1:
        x1 = coords[0][0]
        y1 = coords[0][1]
        x2 = coords[0][2] + x1
        y2 = coords[0][3] + y1
    final_photo = cv2.rectangle(photo, (x1,y1),(x2,y2),(0,255,0),5)
    final_photo = cv2.flip(final_photo, 1)
    cv2.imshow('Video', final_photo)
    if cv2.waitKey(1) == 13:
        break
cv2.destroyAllWindows()
cap.release()


