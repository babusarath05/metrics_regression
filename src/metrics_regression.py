# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 16:48:56 2022

@author: sarathbabu.karunanit
"""

from math import sqrt
from sklearn.metrics import r2_score,mean_squared_error

def adj_r2_score(y_test,y_pred,x):
    num=len(x)-1
    den=len(x)-x.shape[1]-1
    
    adj_r2=(1-r2_score(y_test,y_pred))*(num/den)
    adj_r2=1-adj_r2
    
    return adj_r2
    
def rmse(y_test,y_pred):
    return sqrt(mean_squared_error(y_test,y_pred))