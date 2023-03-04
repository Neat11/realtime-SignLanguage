# import tensorflow as tf
# import numpy as np

# actions = np.array(['hello',"iLoveYou",'okay'])
# model = tf.keras.Sequential()
# model.add(tf.keras.layers.LSTM(64,return_sequences=True, activation='relu', input_shape =(30,258)))
# model.add(tf.keras.layers.LSTM(128,return_sequences=True, activation='relu'))
# model.add(tf.keras.layers.LSTM(64,return_sequences=False, activation='relu'))
# model.add(tf.keras.layers.Dense(64,activation='relu'))
# model.add(tf.keras.layers.Dense(32,activation='relu'))
# model.add(tf.keras.layers.Dense(actions.shape[0], activation='softmax'))
# model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
# model.load_weights('action.h5')
# model.predict()