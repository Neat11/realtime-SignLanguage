import os
import numpy as np
import mediapipe as mp
DATA_PATH = os.path.join('MP_DATA')
actions = np.array(['hello',"iLoveYou",'okay', 'help', 'please', 'thankyou','play'])
no_sequences = 30
sequence_length =30
for action in actions:
        for sequence in range(no_sequences):
            try:
                os.makedirs(os.path.join(DATA_PATH,action,str(sequence)))
            except:
                pass