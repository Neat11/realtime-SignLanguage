import os
import cv2
import numpy as np
from LanguageRecognition import LanguageRecognition
import mediapipe as mp
DATA_PATH = os.path.join('MP_DATA')
actions = np.array(['hello',"LoveYou"])
no_sequences = 30
sequence_length =30
cap = cv2.VideoCapture(0)
mp_holistic = mp.solutions.holistic #bringing a holistic model
mp_drawing = mp.solutions.drawing_utils #drawing utilities
obj = LanguageRecognition()
with mp_holistic.Holistic(min_detection_confidence =0.5, min_tracking_confidence =0.5) as holistic:
    for action in actions:
        for sequence in range(no_sequences):
            try:
                os.makedirs(os.path.join(DATA_PATH,action,str(sequence)))
            except:
                pass
            for frame in range(sequence_length):
                image, results = obj.getFrame(cap,holistic)
                
                if( frame == 0):
                    cv2.putText(image,"Starting now",(120,200))
                    cv2.putText(image,"collecting data for {} video number {}".format(action,sequence),(15,12),)
                    cv2.waitKey(2000)
                else:
                    cv2.putText(image,"collecting data for {} video number {}".format(action,sequence),(15,12),)
                
                keypoints = obj.extract_keypoints(results)
                npy_path = os.path.join(DATA_PATH,action,str(sequence),str(frame))
                np.save(npy_path,keypoints)

                if(cv2.waitKey(10) and 0xFF == ord('q')):
                    break
    cap.release()
    cv2.destroyAllWindows()
