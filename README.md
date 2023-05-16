# chi2_and_CrammerV_Corelation
This repository consists of a Chi2 Correlation and Crammer V Correlation

**Below is the explanation for CramerV correlation code**

## Introduction
This technical document provides an overview of the code that calculates Cramer's V correlation coefficient and generates a heatmap to visualize the correlation between a categorical variable of interest and other categorical variables. The code is written in Python and utilizes libraries such as pandas, numpy, scipy.stats, matplotlib, and seaborn.


### Data Input Format:
  - Requires categorical columns
  - Removing all the null values in all the columns

## Code Description
The provided code consists of two main functions: `cramerV` and `plot_cramer`.
#### 1. `cramerV` Function
The `cramerV` function calculates the Cramer's V correlation coefficient between two categorical variables. Here's a breakdown of the steps involved:
  -	Input: `label` - The categorical variables to be used as the label or target variables.
  -	Input: `x` - The categorical variable to be correlated with the label variables.
  -	`confusion_matrix`: Creates a contingency table using the `pd.crosstab` function to count the occurrences of each combination of labels and variables.
  -	`chi2`: Calculates the Chi-Square statistic using `chi2_contingency` from the scipy.stats module on the created confusion matrix.
  -	`n`: Calculates the sum of all values in the confusion matrix.
  -	`r` and `k`: Retrieves the shape of the confusion matrix to determine the number of rows and columns.
  -	`phi2`: Calculates the phi-squared coefficient by dividing the Chi-Square statistic by the sum of all values in the confusion matrix.
  -	`phi2corr`: Adjusts the phi-squared coefficient by subtracting the correction factor based on the number of rows and columns in the confusion matrix.
  -	`rcorr` and `kcorr`: Apply corrections to the number of rows and columns in the confusion matrix.
  -	`v`: Calculates Cramer's V coefficient by taking the square root of the adjusted phi-squared coefficient divided by the minimum of (kcorr - 1) and (rcorr - 1).
  •	Returns: The calculated Cramer's V coefficient.

#### 2. `plot_cramer` Function
The `plot_cramer` function generates a heatmap that visualizes the Cramer's V correlation coefficients between the column of interest and other columns in the DataFrame. Here's an overview of the steps involved:

  -	Input: `df` - The DataFrame containing the categorical variables.
  -	Input: `column_of_interest` - The column of interest to be correlated with other columns.
  -	`temp`: A temporary dictionary to store the correlation coefficients of each column (excluding the column of interest).
  -	`cramer`: A DataFrame initialized with NaN values to store the correlation coefficients.
  -	`columns`: Retrieves all the column names from the DataFrame.
  -	Loop: Iterates through each column in the DataFrame.
    -	Calculates the correlation coefficient using the `cramerV` function.
    -	Populates the `cramer` DataFrame with the correlation coefficient.
    -	Stores the correlation coefficient in the `temp` dictionary.
  -	Fills NaN values in the `cramer` DataFrame with np.nan.
  -	Plots a heatmap using the `sns.heatmap` function to visualize the correlation coefficients.
  -	Prints the top five columns with the highest correlation coefficients.
  -	Output: Displays the heatmap and the top five correlated columns.

## Correlation Plot:
The range of correlation is from 0 to 1. With 0 means no correlation and the association between two columns increased as the value increases from 0 to 1.


