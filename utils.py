import numpy as np
import pandas as pd




def to_sequences(dataset, seq_size=1):
    #seq_size is the number of previous time steps to use as 
    #input variables to predict the next time period.

    #creates a dataset where X is the number of passengers at a given time (t, t-1, t-2...) 
    #and Y is the number of passengers at the next time (t + 1).
    x = []
    y = []

    for i in range(len(dataset)-seq_size-1):
        #print(i)
        window = dataset[i:(i+seq_size), 0]
        x.append(window)
        y.append(dataset[i+seq_size, 0])
        
    return np.array(x),np.array(y)