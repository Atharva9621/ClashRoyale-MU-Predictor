import numpy as np
import pickle
import os
#total no. of cards 
vector_max = 120    

with open('cr_app/rf_cr_model.sav', 'rb') as file:
    pickle_model = pickle.load(file)
    
def predictionModel(cardList, oppCardList):
    arr1 = np.asarray(cardList).reshape(1, -1)
    arr2 = np.asarray(oppCardList).reshape(1, -1)
    one_hot_wins = np.zeros((1, vector_max+1))
    one_hot_losses = np.zeros((1, vector_max+1))
    one_hot_wins[np.arange(1).reshape(1, -1), arr1]=1
    one_hot_losses[np.arange(1).reshape(1, -1), arr2]=1
    one_hot_arr = np.concatenate((one_hot_wins, one_hot_losses), axis=1)
    # print(one_hot_arr.shape)
    return pickle_model.predict(one_hot_arr)[0]
