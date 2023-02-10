import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import os
from env import host, username, password

#----------------------------------------------------------    

def get_connection(db, user=username, host=host, password=password):
    '''
    This functions imports my credentials for the Codeup MySQL server to be used to pull data
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    
#----------------------------------------------------------    
    
#simply copied this for the framework, will be changed for other data
def get_superstore():

    if os.path.isfile('superstore_data.csv'):
        
        df = pd.read_csv('superstore_data.csv')
        df = df.drop(columns='Unnamed: 0')

        return df
    
    else:
        
        url = get_connection('superstore_db')
        query = '''
                SELECT *
                FROM orders
                JOIN customers ON orders.`Customer ID` = customers.`Customer ID`
                JOIN categories ON orders.`Category ID` = categories.`Category ID`
                JOIN products ON orders.`Product ID` = products.`Product ID`
                JOIN regions ON orders.`Region ID` = regions.`Region ID`;
                '''
        df = pd.read_sql(query, url)                
        df.to_csv('superstore_data.csv')

        return df

#---------------------------------------------------------- 

def wrangle_superstore():
    
    df = get_superstore()
    
    cols_to_drop = ['Region ID', 'Category ID', 'Product ID', 'Customer ID']
    df = df.drop(columns=cols_to_drop)
    
    df['Order Date'] = pd.to_datetime(df['Order Date'], infer_datetime_format=True)
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], infer_datetime_format=True)
    
    df = df.set_index('Order Date')
    df = df.sort_index()

    df = df.rename(columns={
                        'Order Date':'order_date',
                        'Ship Date':'ship_date',
                        'Ship Mode':'ship_mode',
                        'Segment':'segment',
                        'Country':'country',
                        'City':'city',
                        'State':'state',
                        'Postal Code':'postal_code',
                        'Sales':'sales',
                        'Quantity':'qty',
                        'Discount':'discount',
                        'Profit':'profit',
                        'Customer Name':'cust_name',
                        'Category':'category',
                        'Sub-Category':'sub_category',
                        'Product Name':'product_name',
                        'Region Name':'region_name'
                        })

#---------------------------------------------------------- 

def remove_outliers(df, k, col_list):
    ''' 
    This function takes in a dataframe, the threshold and a list of columns 
    and returns the dataframe with outliers removed
    '''   
    for col in col_list:

        q1, q3 = df[col].quantile([.25, .75])  # get quartiles
        
        iqr = q3 - q1   # calculate interquartile range
        
        upper_bound = q3 + k * iqr   # get upper bound
        lower_bound = q1 - k * iqr   # get lower bound

        # return dataframe without outliers
        
        df = df[(df[col] > lower_bound) & (df[col] < upper_bound)]
        
    return df

#---------------------------------------------------------- 



#---------------------------------------------------------- 



#---------------------------------------------------------- 



#---------------------------------------------------------- 

