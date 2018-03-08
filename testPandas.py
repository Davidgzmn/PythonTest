import pandas as pd
from matplotlib import pyplot as plt


rawData = pd.read_csv('/Users/david/Documents/GitHub/DataAnalysis/mm_master_demos.csv', index_col = 0)


print(rawData.head())
