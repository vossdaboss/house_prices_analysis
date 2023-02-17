import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

# We will use the data set to find and remove outliers and df has 1460 rows and 81 columns
df = pd.read_csv('data_archive/train.csv')

# Select the 'GrLivArea' and 'SalePrice' columns from the dataframe
df[["GrLivArea", "SalePrice"]]

# Remove the outliers from the dataframe
df = df.drop(df[df['GrLivArea']>4000].index)

# Plot the data again to see if the outliers have been removed
sns.jointplot(x=df['GrLivArea'], y=df['SalePrice'])
plt.show()