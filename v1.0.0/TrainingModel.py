from sklearn.model_selection import train_test_split
import numpy as np
import tensorflow as tf
import os
from keras.callbacks import TensorBoard

DATA_PATH = os.path.join('v1.0.0/MP_DATA/')
actions = np.array(['hello',"iLoveYou",'okay', 'help', 'please', 'thankyou','play', 'fosshack3'])
no_sequences = 30
sequence_length =30

label_map = {label: num for num, label in enumerate(actions)}
print(label_map)

sequences, labels = [],[]


for action in actions:
    for sequence in range (no_sequences):
        window =[]
        for frame_num in range(sequence_length):
            res = np.load(os.path.join(DATA_PATH,action,str(sequence),"{}.npy".format(frame_num)))
            print(res)
            window.append(res)
            break
        sequences.append(window)
        labels.append(label_map[action])
        break
    break

print(np.shape(np.array(sequences)))
print(np.shape(np.array(labels)))

# x=np.array(sequences)
# y = tf.keras.utils.to_categorical(labels).astype(int)

# print(x.shape)
# print("//////////////////////////////////////////////////////////////////////")
# print(y.shape)


# x_train, x_test,y_train, y_test = train_test_split(x,y, test_size=0.05)
# print(x_train.shape)
# print(y_train.shape)
# print(x_test.shape)
# print(y_test.shape)

# log_dir = os.path.join("Logs")
# tb_callback = TensorBoard(log_dir=log_dir)


# model = tf.keras.Sequential()
# model.add(tf.keras.layers.LSTM(64,return_sequences=True, activation='relu', input_shape =(30,258)))
# model.add(tf.keras.layers.LSTM(128,return_sequences=True, activation='relu'))
# model.add(tf.keras.layers.LSTM(64,return_sequences=False, activation='relu'))
# model.add(tf.keras.layers.Dense(64,activation='relu'))
# model.add(tf.keras.layers.Dense(32,activation='relu'))
# model.add(tf.keras.layers.Dense(actions.shape[0], activation='softmax'))

# model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
# model.fit(x_train, y_train, epochs=2000, callbacks=[tb_callback])

# # model.load_weights('action2.h5')
# model.save('action2.h5')
# model.summary() 


# res = model.predict(x_test)
# print(actions[np.argmax(res[4])])
# print(actions[np.argmax(res[0])])
# print(actions[np.argmax(res[2])])
# print(actions[np.argmax(res[1])])
# print(actions[np.argmax(res[3])])
