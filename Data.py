import os
import numpy as np
DATA_PATH = os.path.join('MP_DATA')
actions = np.array(['hello','thanks','I love you'])
no_sequences = 30
sequence_length =30

for action in actions:
    for sequence in range(no_sequences):
        try:
            os.makedirs(os.path.join(DATA_PATH,action,str(sequence)))
        except:
            pass
