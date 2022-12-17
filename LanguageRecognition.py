import cv2
import numpy as np
import os
import mediapipe as mp
import tensorflow as tf
class LanguageRecognition:
    actions = np.array(['hello',"iLoveYou",'okay'])
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.LSTM(64,return_sequences=True, activation='relu', input_shape =(30,258)))
    model.add(tf.keras.layers.LSTM(128,return_sequences=True, activation='relu'))
    model.add(tf.keras.layers.LSTM(64,return_sequences=False, activation='relu'))
    model.add(tf.keras.layers.Dense(64,activation='relu'))
    model.add(tf.keras.layers.Dense(32,activation='relu'))
    model.add(tf.keras.layers.Dense(actions.shape[0], activation='softmax'))
    model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
    model.load_weights('action.h5')

    DATA_PATH = os.path.join('MP_DATA')
    actions = np.array(['hello',"iLoveYou",'okay'])
    no_sequences = 30
    sequence_length =30
    cap = cv2.VideoCapture(0)
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
        sequence =[]
        sentence =[]
        treshold =0.4
        with self.mp_holistic.Holistic(min_detection_confidence =0.5, min_tracking_confidence =0.5) as holistic:        
            while (self.cap.isOpened()):
                image, results = self.getFrame(self.cap,holistic)
                keypoints = self.extract_keypoints(results)
                sequence.append(keypoints)
                sequence = sequence[-30:]
                if(len(sequence)==30):
                    res = self.model.predict(np.expand_dims(sequence, axis=0))[0]
                    print(self.actions[np.argmax(res)])
                cv2.imshow("Open cv frame", image)
                if(cv2.waitKey(5) and 0xFF == ord('q')):
                    break
        self.cap.release()
        cv2.destroyAllWindows()
        
    def __init__(self) -> None:
        pass

obj = LanguageRecognition()
obj.startCapture()