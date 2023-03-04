import os
import numpy as np
import mediapipe as mp
DATA_PATH = os.path.join('MP_Data_New_Trained')
actions = np.array(['hello',"iLoveYou",'okay', 'help', 'please', 'thankyou','play','fosshack3'])
no_sequences = 30
sequence_length =30
for action in actions:
        for sequence in range(no_sequences):
            try:
                os.makedirs(os.path.join(DATA_PATH,action,str(sequence)))
            except:
                pass


def createUserFile(action: str):
        DATA_PATH = os.path.join('MP_Data_New_Trained')
        no_sequences = 30
        sequence_length =30
        for sequence in range(no_sequences):
                try:
                    os.makedirs(os.path.join(DATA_PATH,action,str(sequence)))
                except:
                    pass
