# Local regression analysis
### Description

This project was done as a part of the course BERN02 at Lund University. The aim of the exercise was to use local regression with one predictor to predict the response for three values for which the prediction is made. More spefically, the aim was to predict total age-adjusted mortality rate per 100,000 for an area with 10, 18 and 25 % of families with income < $3000.



### Data

The data used in this exercise is an airpollution data set from a paper on ridge regression. Source: McDonald, G.C. and Schwing, R.C. (1973) ‘Instabilities of regression estimates relating air pollution to mortality’, Technometrics, vol.15, 463-482.

 - Predictor: % of families with income < $3000 (POOR)
 - Response: Total age-adjusted mortality rate per 100,000 (MORT) 

### Requirements

Packages used in this project are the following:

 - matplotlib
 - numpy
 - pandas
 - pooch
 - scipy

Minimum constraints can be found in the pyproject.toml file. The current constraints are minimum-version constraints rather than exact pinning. This allows unnecesarily restricting the environment to one exact package version but runs the risk of the program breaking or behaving unexpecteadly using future versions of packages. If this happens, the exact versions of the dependencies used to create the current environment can be recreated from the uv.lock file.

The project uses uv for environment management.

### License

The project is licensed under GNU General Public License v3.0. See the LICENSE file for more details.
