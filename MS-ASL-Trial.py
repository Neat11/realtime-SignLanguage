import time
import cv2
from cap_from_youtube import cap_from_youtube
import mediapipe as mp
import numpy as np
import os
import json

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic

DATA_PATH = os.path.join('MS-ASL-RawData')
actions = np.array([])

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

def recordMovements(results):
            lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3)
            rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3)
            return(np.concatenate([lh,rh]))

def GetDataFromVideos(obj):
    youtube_url = obj['url']
    try:
        cap = cap_from_youtube(youtube_url, 'best')
        sequence= []
        with mp_holistic.Holistic(min_detection_confidence =0.7, min_tracking_confidence =0.5) as holistic:  
            cv2.namedWindow('video', cv2.WINDOW_NORMAL)
            time.sleep(1)
            startFrame = obj['start_time'] * obj['fps']
            endFrame = startFrame+29
            frameNumber = startFrame
            while True:
                    if(frameNumber<= endFrame):
                        ret, frame = cap.read()
                        try:   
                            image, results = mediapipe_detection(frame, holistic)
                            draw_landmarks(image, results)
                            sequence.append(recordMovements(results))
                        except:
                            print("some error occured")
                        frameNumber+=1
                    else:
                        print("done with 30 frames")
                        break

                    if not ret:
                        break
                    cv2.imshow('video', image)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
        lmao = np.array(sequence)
        print(len(lmao))
        print(lmao.shape)
        npyPath = os.path.join(DATA_PATH, obj['text'],"0")
        os.makedirs(npyPath)
        for x in range(len(lmao)):
            np.save(os.path.join(npyPath,str(x)), x)
        np.append(actions, obj['text'])
        cap.release()
        cv2.destroyAllWindows()
    except:
        print("video not parsable")


file = open('MS-ASL/MSASL_train.json')
data = json.load(file)
for x in data:
    GetDataFromVideos(x)
np.save("actionsArrayModified.npy", actions)