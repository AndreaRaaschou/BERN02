# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 11:17:05 2026
@author: andrearaaschou

Exercise on GLM's for the course BERN02
"""
import numpy as np
import  matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import minimize

# Read data, put in pandas dataframe
df = pd.read_csv("/Users/andrearaaschou/courses/BERN02/exercises/glm/data/bird_count.csv")
df = df.sort_values("yr").reset_index(drop=True)        # sort data by year (in chronological order) + reset index
df["yr_mean_centered"] = df["yr"] - df["yr"].mean()     # create mean-centered year column


def simulate_bird_counts(df):
    x = df["yr_mean_centered"]
    y = df["count"]
    
    # Estimate intercept and slope using scipy minimize and likelihood function for poisson GLM
    b0, b1 = minimize(lambda beta: -log_likelihood(beta, x, y), x0=[0, 0]).x
    
    # Link function to extract expected responsevalues, used to simulate bird counts
    lambdas = np.exp(b0 + b1*x)
    
    # Plot line for extimated GLM
    plt.plot(df["yr"], np.exp(b0 + b1*x), label = f"Fitted GLM e^({b0:.4f} + {b1:.4f}*x)")
    
    # Generate poisson distributed bird counts 3 times
    result = []
    for i in range(3):
        result.append(np.random.poisson(lambdas))
        
    return result

def log_likelihood(beta, x, y):
    b0, b1 = beta
    return np.sum(-np.e**(b0 + b1*x) + y*(b0 + b1*x))
    

result = simulate_bird_counts(df)
    
# Save the samples in a csv-file with column headers indicating which sample it is
df_sim = pd.DataFrame(result, index = ["simulation 1", "simulation 2", "simulation 3"]).T
df_sim["yr"] = df["yr"]                                                         # add year column
df_sim = df_sim[["yr", "simulation 1", "simulation 2", "simulation 3"]]         # change order of columns
df_sim.to_csv("simulated_bird_counts.csv", index=False)


# Add to plot to visualize generated bird counts
plt.plot(df["yr"], df["count"], "D", label = "Observed values")
plt.plot(df["yr"], result[0], "o", label = "First simulation")
plt.plot(df["yr"], result[1], "o", label = "Second simulation")
plt.plot(df["yr"], result[2], "o", label = "Third simulation")
plt.legend(bbox_to_anchor = (1.05, 0.6))
plt.title("Observed and simulated bird counts")
plt.xlabel("year")
plt.ylabel("bird count")
plt.show()

