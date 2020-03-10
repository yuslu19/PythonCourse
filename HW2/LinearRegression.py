# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 13:49:59 2020

@author: user
"""
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
df = pd.read_csv('econ.csv')                                #imports the csv file
df1=df.dropna()
x=df1['Total Population']                                   #takes the data column called 'Total Population'
y=df1['GDP']                                                #takes the date column called 'GDP'
def MyFun(x,y):
    x=(x-np.mean(x))/np.std(x)                              #Normalization of x
    y=(y-np.mean(y))/np.std(y)                              #Normalization of y
    a=np.matmul(x.T,x)                          
    b=np.matmul(x.T,y)
#    beta=np.matmul(np.linalg.inv(a),b)                     #Following 3 line is for matrices(nxm) which are not nx1
#    e=y-np.matmul(beta,x)
#    varB=np.matmul(sigma2,np.linalg.inv(a))
    t=stats.t.ppf(0.975,np.size(x)-1)
    beta=b/a                                                #Calculates Beta
    e=y-beta*x                                              #Calculates Error
    sigma2=np.matmul(e.T,e)*(1/(np.size(x)-1))              #Calculates sigma squared
    varB=sigma2*1/a                                         #Calculates variance of Beta
    SEbeta=np.sqrt(varB)
    t1=beta+SEbeta*t
    t2=beta-SEbeta*t
    plt.plot(x,y,'o')                                       #Plots the datas taken from world bank
    plt.plot(x,beta*x+e,'-')                                #Confirms that our beta and error values are calculated correctly
    plt.plot(x,beta*x,'-')                                  #Plots the estimated values
    return(beta,[t1,t2],SEbeta)
MyFun(x,y)