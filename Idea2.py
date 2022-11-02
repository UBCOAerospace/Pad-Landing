import cv2

cap =  cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _= frame.shape
    
    cx = int(width / 2)
    cy = int(height / 2)
    
    pix_cen = hsv[cy, cx]
    print(pix_cen)
    cv2.circle(frame, (cx, cy), 5, (255,0,0), 3)
    
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroAllWindows()