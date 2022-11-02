import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _, frame = cap.read()
    
    frame_grey = cv2.cvtColor(frame, cv.COLOR_BGG2GRAY)
    
    ret, thrash = cv2.threshold()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([100, 100, 60])
    upper_blue = np.array([130, 250, 250])

    mask1 = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame,frame,mask = mask)
    
    M = cv2.moments(mask)
    
    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])
    
    cv2.circle(frame, (cx, cy), 5, (255,255,255), -1)
    cv2.putText(frame, "PAD", (cx -25, cy-25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
    cv2.imshow('frome', frame)

    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroAllWindows()


BGR_color = np.array([[[255,0,0]]])
x=cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV)
x[0][0]