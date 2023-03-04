import numpy as np
import createfiles
# actions =np.array(['hello',"iLoveYou",'okay', 'helps', 'please', 'thankyou','play'])

# np.save("actionsArray.npy", actions )


createfiles.createUserFile("lmaooo")
actions = np.load('actionsArray.npy')
print(actions)