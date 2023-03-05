import os
import numpy as np
import cv2
import mediapipe as mp
DATA_PATH = os.path.join('MP_Data_New_2')
actions = np.load('actionsArray.npy')
no_sequences = 30
sequence_length =30
cap = cv2.VideoCapture(0)
mp_holistic = mp.solutions.holistic #bringing a holistic model
mp_drawing = mp.solutions.drawing_utils #drawing utilities
def mediapipe_detection(image,model):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = model.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        return image, results
def draw_landmarks(image, results):
        if(results.left_hand_landmarks):
            mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        if(results.right_hand_landmarks):
            mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        # mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
        #                         mp_drawing.DrawingSpec(color=(80,22,10), thickness=2, circle_radius=4), 
        #                         mp_drawing.DrawingSpec(color=(80,44,121), thickness=2, circle_radius=2)
        #                         )
        # mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION, 
        #                          mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1), 
        #                          mp_drawing.DrawingSpec(color=(80,256,121), thickness=1, circle_radius=1)
        #                          ) 
def extract_keypoints(results):
        lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3)
        rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3)
        return np.concatenate([lh, rh])

with mp_holistic.Holistic(min_detection_confidence =0.5, min_tracking_confidence =0.5) as holistic:
    for action in actions:
            input("enter any key to start {}".format(action))
            for sequence in range(no_sequences):
                for frame_num in range(sequence_length):
                        ret, frame =cap.read()
                        image, results = mediapipe_detection(frame, holistic)
                        draw_landmarks(image, results)
                         
                        if(frame_num == 0):
                            cv2.putText(image,"Starting now",(120,200), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),4,cv2.LINE_AA)
                            cv2.putText(image,"collecting data for {} video number {}".format(action,sequence),(15,12),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),2,cv2.LINE_4)
                            cv2.waitKey(2000)
                        else:
                            cv2.putText(image,"collecting data for {} video number {}".format(action,sequence),(15,12),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),4,cv2.LINE_4)
                                 
                        keypoints = extract_keypoints(results)
                        npy_path = os.path.join(DATA_PATH,action,str(sequence),str(frame_num))
                        np.save(npy_path,keypoints)
                        cv2.imshow("opencv feed", image)
                        if(cv2.waitKey(5)%256 == 27):
                            break
    cap.release()
    cv2.destroyAllWindows()
