import cv2
import numpy
import time

cap = cv2.VideoCapture(-1)

rectangle = []

while cap.isOpened():
    _, frame = cap.read()


    mong = cv2.medianBlur(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 5)
    circles = cv2.HoughCircles(mong, cv2.HOUGH_GRADIENT, 1, 10)# ret=[[Xpos,Ypos,Radius],...]

    # print(rectangle)
    if len(rectangle) > 0:
        rec = rectangle[0]
        cv2.rectangle(mong, (rec[0], rec[1]), (rec[2], rec[3]), color=(255, 255, 255), thickness=3)
    if len(rectangle) > 1:
        rectangle.pop(0)

    # cv2.rectangle(mong, (0, 0), (50, 50), color=(0,0,255), thickness=3)
    # cv2.rectangle(mong, (150, 150), (250, 250), color=(0,0,255), thickness=3)

    # cv2.rectangle(mong, (0, 0), (100, 100), color=(0, 0, 255), thickness=3)
    # print(circles, type(circles))
    if type(circles) is numpy.ndarray:
        rad = int(circles[0][0][2]) + 10
        rectangle.append([int(circles[0][0][0])-rad, int(circles[0][0][1])-rad, int(circles[0][0][0])+rad, int(circles[0][0][1])+rad])
        # time.sleep(2)
    
    cv2.imshow('Video', mong)

    # time.sleep(0.3)
    if cv2.waitKey(1)==27:# esc Key
        break

cap.release()
cv2.destroyAllWindows()