import cv2

cap = cv2.VideoCapture(0)
while (cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow("opencv frame", frame)
    if(cv2.waitKey(10) and 0xFF == ord('q')):
        break
