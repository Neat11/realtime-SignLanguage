import os
import numpy as np
import mediapipe as mp
DATA_PATH = os.path.join('MP_DATA')
actions = np.load('actionsArray.npy')
no_sequences = 30
sequence_length =30
for action in actions:
        for sequence in range(no_sequences):
            try:
                os.makedirs(os.path.join(DATA_PATH,action,str(sequence)))
            except:
                pass

            
def createUserFile(action: str):
        ll = np.append(actions, [action])
        print(ll)
        DATA_PATH = os.path.join('MP_Data_New_Trained')
        no_sequences = 30
        sequence_length =30
        for sequence in range(no_sequences):
                try:
                    os.makedirs(os.path.join(DATA_PATH,action,str(sequence)))
                except:
                    pass
        np.save('actionsArray.npy', ll)