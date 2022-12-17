import pyvirtualcam
import cv2

class Webcam:
    
    def addString(string):
        fmt = pyvirtualcam.PixelFormat.BGR
        with pyvirtualcam.Camera(width=1280, height=720, fps=20, fmt=fmt) as cam:
            while True:
                ret_val,frame = cv2.VideoCapture(0).read()
                x,y = 640-len(string)*10,670
                frame = cv2.resize(frame, (1280, 720), interpolation=cv2.BORDER_DEFAULT)
                cv2.putText(frame,f"{len(string)},{y}",(50,50),3,1,(0,0,0),1,cv2.LINE_8)
                cv2.putText(frame,string,(x,y),3,1,(0,0,0),1,cv2.LINE_8)
                frame = cv2.flip(frame,1)
                cam.send(frame)
                cam.sleep_until_next_frame()
                if cv2.waitKey(10) == 27:
                    break  # esc to quit
            cv2.destroyAllWindows()

Webcam.addString("Hello")