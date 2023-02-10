import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import mean_squared_error
from math import sqrt 

import statsmodels.api as sm
from statsmodels.tsa.api import Holt, ExponentialSmoothing
np.random.seed(42)
#---------------------------------------------------------

def evaluate(target_var, yhat_df, validate):
    '''
    This function will take the actual values of the target_var from validate, 
    and the predicted values stored in yhat_df, 
    and compute the rmse, rounding to 0 decimal places. 
    it will return the rmse. 
    '''
    rmse = round(sqrt(mean_squared_error(validate[target_var], yhat_df[target_var])), 2)
    return rmse

#---------------------------------------------------------

def plot_and_eval(train, validate, yhat_df, target_var):
    '''
    This function takes in the target var name (string), and returns a plot
    of the values of train for that variable, validate, and the predicted values from yhat_df. 
    it will als lable the rmse. 
    '''
    for col in train.columns:
    
        plt.figure(figsize = (12,4))
        plt.plot(train[col], label='Train', linewidth=1, color='#377eb8')
        plt.plot(validate[col], label='Validate', linewidth=1, color='#ff7f00')
        plt.plot(yhat_df[col], label='yhat', linewidth=2, color='#a65628')
        plt.legend()
        plt.title('Average Temperature')
        rmse = evaluate('avg_temp', yhat_df, validate)
        print(col, '-- RMSE: {:.0f}'.format(rmse))
        plt.show()

#---------------------------------------------------------

def append_eval_df(model_type, target_var, eval_df, rmse):
    '''
    this function takes in as arguments the type of model run, and the name of the target variable. 
    It returns the eval_df with the rmse appended to it for that model and target_var. 
    '''
    d = {'model_type': [model_type], 'target_var': [target_var],
        'rmse': [rmse]}
    d = pd.DataFrame(d)
    return eval_df.append(d, ignore_index = True)

#---------------------------------------------------------

def make_baseline_predictions(sales_predictions=None, quantity_predictions=None):
    yhat_df = pd.DataFrame({'avg_temp': [avg_temps],
                           'avg_temp_uncertainty': [avg_temps_uncertainty]},
                          index=validate.index)
    return yhat_df

#---------------------------------------------------------



#---------------------------------------------------------



#---------------------------------------------------------



#---------------------------------------------------------
