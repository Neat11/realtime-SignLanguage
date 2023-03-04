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


# import time
# import cv2
# from cap_from_youtube import cap_from_youtube

# youtube_url = 'https://www.youtube.com/watch?v=PIsUJl8BN_I'
# cap = cap_from_youtube(youtube_url, 'best')

# cv2.namedWindow('video', cv2.WINDOW_NORMAL)
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#     cv2.imshow('video', frame)
#     time.sleep(0.06)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break




import time
import cv2
from cap_from_youtube import cap_from_youtube
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic



def mediapipe_detection(image,model):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = model.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        image = cv2.resize(image, (1280, 720))
        return image, results



def draw_landmarks(image, results):
        if(results.left_hand_landmarks):
            mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        if(results.right_hand_landmarks):
            mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

youtube_url = 'https://www.youtube.com/watch?v=PIsUJl8BN_I'
cap = cap_from_youtube(youtube_url, 'best')

def recordMovements(results):
            lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3)
            rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3)
            return(np.concatenate([lh,rh]))
sequence=[]
with mp_holistic.Holistic(min_detection_confidence =0.7, min_tracking_confidence =0.5) as holistic:  
  cv2.namedWindow('video', cv2.WINDOW_NORMAL)
  time.sleep(1)
  while True:
        ret, frame = cap.read()
        try:   
            image, results = mediapipe_detection(frame, holistic)
            draw_landmarks(image, results)
            sequence.append(recordMovements(results))
        except:
             print("some error occured")

        if not ret:
            break
        cv2.imshow('video', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
print(len(sequence))
print(sequence)
cap.release()
cv2.destroyAllWindows()