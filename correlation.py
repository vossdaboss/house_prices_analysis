import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

df = pd.read_csv('data_archive/house_prices_dataset/train.csv')

# Select the columns with numeric data types from the 'df' dataframe
numeric_data = df.select_dtypes(include=[np.number])

# Select the columns with non-numeric (categorical) data types from the 'df' dataframe
catagorical_data = df.select_dtypes(exclude=[np.number])

# Remove the 'Id' column from the 'numeric_data' dataframe
del numeric_data['Id']

# Compute the correlation matrix of the 'numeric_data' dataframe
corr = numeric_data.corr()

# Create a heatmap of the correlation matrix using seaborn
plt.figure(figsize=(10, 10))
sns.heatmap(corr)

# Print the 10 highest correlations with 'SalePrice'
print(corr['SalePrice'].sort_values(ascending=False)[:10])

# Print the 5 correlations with 'SalePrice' that are greater than 0.5 and less than or equal to 0.7
print(corr['SalePrice'].sort_values(ascending=False)[5:])
