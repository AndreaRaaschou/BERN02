# Soil Organic Carbon Prediction with Neural Networks

## Overview
This project investigates whether climate and soil properties can be used to predict soil organic carbon (SOC) in the upper 100 cm of soil across the Northern circumpolar region. A neural network is trained and evaluated using spatially separated training, validation, and test sets.

## Data
The project combines:
- **BERN01:** Climate data and soil properties
- **NCSCDv2:** Soil organic carbon and non-soil coverage data.

Data files are stored in the `data/` directory and are not included in this repository since some of the files are too large to push.

## Repository Structure
- `main.ipynb` — Data processing, exploration, model training, and evaluation.
- `Geographical_CV.ipynb` — Alternative geographical validation approach.
- `remove_outliers.ipynb` — Investigation of outlier removal.
- `plots/` — Figures generated during the project.

## Method
Climate variables are aggregated into annual features. A geographical region is held out for testing, and neural networks with and without dropout are compared. Sample weights based on non-soil coverage are used during training.

## Requirements
Python with NumPy, pandas, xarray, Matplotlib, Cartopy, TensorFlow, and scikit-learn.

## Usage
Place the required data files in `data/` and run `main.ipynb` from top to bottom.
