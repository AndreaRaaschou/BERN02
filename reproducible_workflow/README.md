# Local regression analysis
## Description

This project was done as a part of the course BERN02 at Lund University. The aim of the exercise was to use local regression with one predictor to predict the response for three values for which the prediction is made. More spefically, the aim was to predict Total age-adjusted mortality rate per 100,000 for an area with 10, 18 and 25 % of families with income < $3000.



## Data

The data used in this exercise is an airpollution data set from a paper on ridge regression. Source: McDonald, G.C. and Schwing, R.C. (1973) ‘Instabilities of regression estimates relating air pollution to mortality’, Technometrics, vol.15, 463-482.

Predictor: % of families with income < $3000 (POOR)
Response: Total age-adjusted mortality rate per 100,000 (MORT) 

## Requirements

Packages used in this project are the following:

 - matplotlib
 - numpy
 - pandas
 - pooch
 - scipy

Pinned versions can be found in the .toml file.

The project uses uv for environment management.