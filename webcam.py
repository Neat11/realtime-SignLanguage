import numpy as np
# actions =np.array(['hello',"iLoveYou",'okay', 'helps', 'please', 'thankyou','play'])

# np.save("actionsArray.npy", actions )


actions = np.load('actionsArray.npy')
actions = np.delete(actions, 14)
print(actions)
np.save('actionsArray.npy',actions)

