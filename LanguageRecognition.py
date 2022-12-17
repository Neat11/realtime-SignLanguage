import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import mediapipe as mp

class LanguageRecognition:
    DATA_PATH = os.path.join('MP_DATA')
    actions = np.array(['hello',"iLoveYou"])
    no_sequences = 30
    sequence_length =30
    cap = cv2.VideoCapture(0)

    def train(self):
        with self.mp_holistic.Holistic(min_detection_confidence =0.5, min_tracking_confidence =0.5) as holistic:
            for action in self.actions:
                for sequence in range(self.no_sequences):
                    try:
                        os.makedirs(os.path.join(self.DATA_PATH,action,str(sequence)))
                    except:
                        pass
                    for frame in range(self.sequence_length):
                        image, results = obj.getFrame(self.cap,holistic)
                        
                        if( frame == 0):
                            cv2.putText(image,"Starting now",(120,200), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),4,cv2.LINE_AA)
                            cv2.putText(image,"collecting data for {} video number {}".format(action,sequence),(15,12),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),4,cv2.LINE_AA)
                            cv2.waitKey(2000)
                        else:
                            cv2.putText(image,"collecting data for {} video number {}".format(action,sequence),(15,12),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),4,cv2.LINE_AA)
                        
                        keypoints = obj.extract_keypoints(results)
                        npy_path = os.path.join(self.DATA_PATH,action,str(sequence),str(frame))
                        np.save(npy_path,keypoints)

                        if(cv2.waitKey(10) and 0xFF == ord('q')):
                            break
            self.cap.release()
            cv2.destroyAllWindows()


    mp_holistic = mp.solutions.holistic #bringing a holistic model
    mp_drawing = mp.solutions.drawing_utils #drawing utilities
    def mediapipe_detection(self,image,model):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = model.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        return image, results

    def draw_landmarks(self,image, results):
        if(results.left_hand_landmarks):
            self.mp_drawing.draw_landmarks(image, results.left_hand_landmarks, self.mp_holistic.HAND_CONNECTIONS)
        if(results.right_hand_landmarks):
            self.mp_drawing.draw_landmarks(image, results.right_hand_landmarks, self.mp_holistic.HAND_CONNECTIONS)
        # mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACE_CONNECTIONS, 
        #                          mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1), 
        #                          mp_drawing.DrawingSpec(color=(80,256,121), thickness=1, circle_radius=1)
        #                          ) 
        # Draw pose connections
        self.mp_drawing.draw_landmarks(image, results.pose_landmarks, self.mp_holistic.POSE_CONNECTIONS,
                                self.mp_drawing.DrawingSpec(color=(80,22,10), thickness=2, circle_radius=4), 
                                self.mp_drawing.DrawingSpec(color=(80,44,121), thickness=2, circle_radius=2)
                                ) 
    def extract_keypoints(self,results):
        lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3)
        rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3)
        pose = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(33*4)
        return np.concatenate([pose,lh, rh])

    def getFrame(self,cap,holistic):
        ret, frame =cap.read()
        image, results = self.mediapipe_detection(frame, holistic)
        self.draw_landmarks(image, results)
        return image,results

    def startCapture(self):
        with self.mp_holistic.Holistic(min_detection_confidence =0.5, min_tracking_confidence =0.5) as holistic:        
            while (self.cap.isOpened()):
                image, results = self.getFrame(self.cap,holistic)
                cv2.imshow("Open cv frame", image)
                if(cv2.waitKey(10) and 0xFF == ord('q')):
                    break
        self.cap.release()
        cv2.destroyAllWindows()
        
    def __init__(self) -> None:
        pass

obj = LanguageRecognition()
obj.startCapture()