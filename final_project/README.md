# Building a Neural Network to Predict Soil Organic Carbon in the Northern Circumpolar Region

## Overview
This project investigates whether climate and soil properties can be used to predict soil organic carbon (SOC) in the upper 100 cm of soil across the Northern circumpolar region. A neural network is trained and evaluated using spatially separated training, validation, and test sets.

## Data
The project combines data from two different sources:
- Climate data and soil properties from the course BERN01 
- Soil organic carbon and non-soil coverage data from The Northern Circumpolar Soil Carbon Database (NCSCD) https://doi.org/10.5879/ecds/00000001 

Data files are stored in the `data/` directory and are not included in this repository since some of the files are too large to push.

## Repository Structure
- `notebooks/`
    - `main.ipynb` — Data processing, exploration, model training, and evaluation.
    - `Geographical_CV.ipynb` — Alternative geographical validation approach.
    - `remove_outliers.ipynb` — Investigation of outlier removal.
- `plots/` — Figures generated during the project.


## Method
Climate variables are aggregated into annual features. A geographical region is held out for testing, and neural networks with and without dropout are compared. Sample weights based on non-soil coverage are used during training.

### Data visualization
Correlation between SOC and the different possible predictors is visualized with scatter-plots. In some of the plots, I added a line showing the linear relationship between the two variables. I also calculated the Spearman correlation between all possible features and SOC to further get an idea of the different interactions and to help me choose the most important features to train the model. SOC and non-soil percentages were visualized in on maps centered around the North Pole. This helps the viewer gain an understanding of both the extension of the area investigated and an idea of how the different metrics varies within the geographical region.  

### Choice of model
The reason for choosing a neural network to solve this problem was mainly for learning purposes, not necessarily because it has the best chance of solving the problem. Since the dataset is limited, and I have a lot of climate features that could help predict SOC that I chose not to use to help keep the amount of parameters within a reasonable amount, a better alternative choice would be to use a Random Forest regression model or a linear model. 

## Usage
Place the required data files in `data/` and run `main.ipynb` from top to bottom.

### Requirements
Python with NumPy, pandas, xarray, Matplotlib, Cartopy, TensorFlow, and scikit-learn.

## FAIR principles
 - **F**indable: The project is public and can be found on GitHub. Data from the NCSCD can be found using the link provided below. Data from the BERN01 course cannot be found publically.
 - **A**ccessible: The code and all the figures are accessible to pull from the public GitHub repository. The data is less accessible (see point above)
 - **I**nteroperable: I have done my best to use formal, accessible and broadly used libraries and vocabulary to make the code easy to understand and for it to work with other applications. References to the NCSCD data is clear, but a clear limitation is the missing data from BERN01. 
 - **R**eusable: This project can not be recreated fully since some of the data is missing. I am currently missing a .venv file which is a limitation for reuse and reproduce the code on another computer. I have used a license which allows for reusing the code. 


