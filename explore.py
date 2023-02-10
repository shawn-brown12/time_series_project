import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#---------------------------------------------------

def subset_time_series(df):
    
    train_len = int(.6 * len(df))
    val_test_split = int(.8 * len(df))
    
    train = df.iloc[:train_len]
    validate = df.iloc[train_len:val_test_split]
    test = df.iloc[val_test_split:]
    
    print(train.shape, validate.shape, test.shape)

    return train, validate, test

#---------------------------------------------------



#---------------------------------------------------



#---------------------------------------------------



#---------------------------------------------------



#---------------------------------------------------
