# import cv2, pafy
# import cap_from_youtube
# url = "https://www.youtube.com/watch?v=C37R_Ix8-qs"
# cap = cap_from_youtube(url,'360p')
# cv2.namedWindow('video', cv2.WINDOW_NORMAL)
# while True:
#   ret, frame = cap.read()
  
#   cv2.imshow('webcam feed' , frame)
#   if cv2.waitKey(1) and 0xFF == ord(' '):
#     break
    
# cap.release()
# cv2.destroyAllWindows()
import time
import cv2
from cap_from_youtube import cap_from_youtube

youtube_url = 'https://www.youtube.com/watch?v=PIsUJl8BN_I'
cap = cap_from_youtube(youtube_url, 'best')

cv2.namedWindow('video', cv2.WINDOW_NORMAL)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('video', frame)
    time.sleep(0.06)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break