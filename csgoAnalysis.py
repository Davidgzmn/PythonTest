import pandas as pd
from matplotlib import pyplot as plt

csgoData = pd.read_csv('/Users/david/Documents/GitHub/DataAnalysis/mm_master_demos.csv')
weapons = csgoData.groupby('wp').csgoData[1].count().reset_index()


#plt.figure()
#ax=plt.subplot()
#ax.set_xticks(range(weapons.nunique()))
#ax.set_xticklabels(weapons.unique(), rotation = 90)
#plt.bar(range(weapons))
#plt.show()
