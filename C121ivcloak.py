import cv2
import time
import numpy as np
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output_file = cv2.VideoWriter("output.avi", fourcc, 20.0, (640,480))
cap = cv2.VideoCapture(0)
time.sleep(2)
bg = 0
for i in range (120):
    ret,bg = cap.read()
bg = np.flip(bg,axis = 1)
while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break
    img = np.flip(img, axis = 1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lowerred = np.array([0,120,50])
    upperred = np.array([10,255,255])
    mask1 = cv2.inRange(hsv,lowerred,upperred)
    lowerred = np.array([170,120,70])
    upperred = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lowerred,upperred)
    mask1 = mask1+mask2
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3,3), np.uint8))
    mask2 = cv2.bitwise_not(mask1)
    result1 = cv2.bitwise_and(img, img, mask = mask2)
    result2 = cv2.bitwise_and(bg, bg, mask = mask1)
    finaloutput = cv2.addWeighted(result1, 1, result2, 1, 0)
    output_file.write(finaloutput)
    cv2.imshow("magic", finaloutput)
    cv2.waitKey(1)
cap.release()
output_file.release()
cv2.destroyAllWindows()