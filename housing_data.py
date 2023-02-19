import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

import os
for dirname, _, filenames in os.walk('data_archive/house_prices_dataset'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
