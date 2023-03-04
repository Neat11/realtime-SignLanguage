import numpy as np
# actions =np.array(['hello',"iLoveYou",'okay', 'helps', 'please', 'thankyou','play'])

# np.save("actionsArray.npy", actions )


actions = np.load('actionsArray.npy')
print(actions)
