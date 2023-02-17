import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

# Visualize Missing Values, outliers, skewed data and correlations using plots and grids 
# to help us understand the data better and make better decisions

# Read the data 
df = pd.read_csv('data_archive/train.csv')

# Calculate the percentage of missing values in each column of the dataframe
missing_values = df.isnull().sum() / len(df)

# Filter out columns with no missing values
missing_values = missing_values[missing_values > 0]

# Sort the columns with missing values in ascending order and print the result
missing_values.sort_values(inplace=True)

# Convert the 'missing_values' series to a new pandas dataframe
missing_values = pd.DataFrame(missing_values)

# Customize the column name to 'count'
missing_values.columns = ['count']

# Customize the index name to 'Name'
missing_values.index.names = ['Name']

# Created Barplot to visualize the missing values
sns.set(style="whitegrid", color_codes=True)
sns.barplot(x=missing_values.index, y=missing_values['count'])
plt.xticks(rotation=90)
print(plt.show())