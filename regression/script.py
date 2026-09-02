# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 10:38:21 2026
@author: andrearaaschou

Exercise on regression for the course BERN02
"""
import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
from scipy.optimize import minimize 

# Read data, put in pandas dataframe
df = pd.read_csv("/Users/andrearaaschou/courses/BERN02/exercises/regression/data/pollution_cleaneddata.csv")

# Vector of values for which the prediction is going to be made
x0 = [10, 18, 25]

def local_regression_prediction(y, x, k, x0):
    """
    Performs predictions with Local regression using one predictor.

    Parameters
    ----------
    y : pandas series
        Vector of observations of the response variable.
    x : pandas series
        Vector of observations of the predictor.
    k : int
        number of neighboring points to include in each local regression and.
    x0 : list
        vector of values for which a prediction is going to be made.

    Returns
    -------
    pred : list
        vector of predicted values.
    se : list
        vector of standard deviations of the expected value of each predicted value.
    """
    
    # Create plot to illustrate datapoints and selected local points
    plt.plot(x, y, ".", label = "Non-selected datapoints")
    plt.title("Visualization of datapoints")
    plt.xlabel("% of families with income < $3000")
    plt.ylabel("Total age-adjusted mortality rate per 100,000")
    
    # Create output lists
    pred = []
    se = []
    
    # Loop through the array x0 and fill arrays pred and se
    for i in range(len(x0)):
        # Select points close to x0
        local_x, local_y = select_neighboring_points(y, x, k, x0[i])
        
        # Mark selected points in plot
        plt.plot(local_x, local_y, "o", label = f"Selected points near x0_{i}")
       
        # Use optimization to estimate the local intercept and slope (b0 and b1)
        w = weight(local_x, x0[i])
        b0, b1 = minimize(weighted_rss, [0,0], args=(local_x, local_y, w)).x
        
        # Plug the estimated beta values into the model y = b0 + x*b1 to get predictions
        pred.append(b0 + b1*x0[i])
        
        # Calculate standard deviation using RSS with my predicted b0 and b1
        variance = np.sum((local_y - (b0 + b1*local_x))**2) / k 
        se.append(np.sqrt(variance)) 
        
    # Add predictions etc to plot
    plt.plot(x0, pred, "bD", label = "Predicted values")
    plt.errorbar(x0, pred, yerr = se, fmt = "bD", capsize = 5)
    plt.legend(bbox_to_anchor=(1.6, 0.7))
    plt.show()
    
    return(pred, se)

def select_neighboring_points(y, x, k, x0):
    # make a new array with the difference between x and x0 (squared)
    diff = (x - x0)**2 
    
    # get indices for the k smallest differences
    indices = np.argsort(diff)[:k]  
    
    # Return the k smallest values in x and y 
    return(x.iloc[indices], y.iloc[indices]) 

def weighted_rss(beta, x, y, w):
    b0, b1 = beta
    return np.sum(w*(y - (b0 + b1*x))**2)
    
def rss(beta, x, y):
    b0, b1 = beta
    return np.sum((y - (b0 + b1*x))**2)

# Assigns a weight to each x_i depending on how close it lies to x_0
def weight(x, x0):
    # Weight is calculates using the squared difference between x and x0
    # If point is close: w is close to 1
    # If point is not close: w is close to 0
    return(1/((x - x0)**2 + 1))

# Create plot to illustrate my weight function
def create_weight_plot():
    x = np.linspace(0, 10, num = 100)
    y = 1/(1+(x)**2)
    plt.plot(x,y)
    plt.title("Illustration of weight function")
    plt.xlabel("(x-x0)**2")
    plt.ylabel("w")
    plt.show()
    

# Run prediction
pred, se = local_regression_prediction(y = df["MORT"], 
                                       x = df["POOR"],
                                       k = 5, 
                                       x0 = x0)

# Print results of prediction
print("Predicted values (± SD) ")
for i in range(len(pred)):
    print(f"x = {x0[i]}%: {pred[i]:.0f} ± {se[i]:.0f}")

create_weight_plot()







