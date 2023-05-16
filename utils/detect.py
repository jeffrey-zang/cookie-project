import cv2
import numpy

cap = cv2.VideoCapture(-1)

rectangle = []

while cap.isOpened():
    _, frame = cap.read()


    frame = cv2.medianBlur(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 5)
    circles = cv2.HoughCircles(frame, cv2.HOUGH_GRADIENT, 1, 10)

    if len(rectangle) > 0:
        rec = rectangle[0]
        cv2.rectangle(frame, (rec[0], rec[1]), (rec[2], rec[3]), color=(255, 255, 255), thickness=3)
    if len(rectangle) > 1:
        rectangle.pop(0)

    if type(circles) is numpy.ndarray:
        rad = int(circles[0][0][2]) + 10
        rectangle.append([int(circles[0][0][0])-rad, int(circles[0][0][1])-rad, int(circles[0][0][0])+rad, int(circles[0][0][1])+rad])
    
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()