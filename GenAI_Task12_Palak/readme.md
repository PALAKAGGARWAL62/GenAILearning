# Assignment 12: Seaborn (Relational, Distribution, Categorical & Multi-Plots)

All code related to this assignment is in Assignment12.ipynb file
How to Execute
Data file Housing.csv must be there in the root folder
Open notebook and execute the code cell by cell to check the output

Dataset Requirement (Mandatory)

1. Go to Kaggle and download any one dataset of your choice.
o Examples (you may choose any):
Student performance dataset
Sales dataset
Insurance dataset
House price dataset
E-commerce dataset
2. Dataset must have:
o At least 2 numerical columns
o At least 1 categorical column
3. Load the dataset using Pandas and use it for all plots below.
(Use the SAME dataset for all tasks unless mentioned)

Restrictions:
Use Seaborn + Pandas + Matplotlib only.
Do NOT use Plotly or other visualization libraries.
Focus on understanding plot purpose, not styling.

## Types of plot
1. Relational Plot
2. Distribution Plot
3. Categorical Plot
4. Regression Plot
5. Matrix Plot
6. Multi Plot

## Task 1: Relational Plot
1. Create a relational plot (relplot) using:
o X-axis → numerical column
o Y-axis → numerical column
2. Use hue with a categorical column.
3. Create the same plot using scatter style.

## Task 2: Line Plot as Scatter & Facet
1. Create a line plot using sns.lineplot().
2. Convert the same relationship into a scatter-style line plot.
3. Use faceting (col or row) to split the plot based on a categorical column.

## Task 3: Distribution Plots
For a numerical column:
1. Plot Histogram using Seaborn.
2. Plot KDE plot.
3. Plot Rug plot.
4. Combine Histogram + KDE in a single plot.

## Task 4: Bivariate Distribution Plots
Using two numerical columns:
1. Create a bivariate histogram.
2. Create a bivariate KDE plot.

## Task 5: Matrix Plots
1. Create a pair plot using sns.pairplot().
2. Create a heatmap of correlation matrix.

## Task 6: Categorical Plots
Using a categorical and numerical column:
1. Bar plot
2. Box plot
3. Violin plot
4. Count plot

## Task 7: Regression Plots
1. Create a regression plot (regplot) between two numerical columns.
2. Create an lmplot with hue using a categorical column.

## Task 8: Multi-Plots & Figure-Level Plots
1. Create a FacetGrid with:
o One numerical variable on x-axis
o One numerical variable on y-axis
o Categorical column as col or row
2. Create a multi-plot dashboard using:
o relplot
o catplot
o displot
