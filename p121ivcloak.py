from cv2 import VideoCapture
import numpy as np
import cv2
video = VideoCapture(0)
image = cv2.imread("rainbow.png")
while True:
    ret,frame = video.read()
    print(frame)
    frame = cv2.resize(frame,(640,480))
    image = cv2.resize(image,(640,480))
    ublack = np.array([104,153,70])
    lblack = np.array([30,30,0])
    mask = cv2.inRange(frame,lblack,ublack)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    f = frame-res
    f = np.where(f == 0, image, f)
    cv2.imshow("video", frame)
    cv2.imshow("mask", f)
    cv2.waitKey(1)
video.release()
cv2.destroyAllWindows()