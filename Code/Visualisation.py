import numpy as np
import pandas as pd
import seaborn as sns

from matplotlib import pyplot as plt
import os

################################
desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',15)
####################


var_2015 = pd.read_csv(r"C:\Users\Aditya\2015.csv")
var_2015 = pd.DataFrame(var_2015)
var_2015 = var_2015.rename({'Country': 'C', 'Region': 'R', 'Happiness Rank': 'Hr', 'Happiness Score': 'Hs',
                        'Standard Error':'Se','Economy (GDP per Capita)':'Ec',
                        'Family':'Fa','Health (Life Expectancy)':'Hl','Freedom':'Fr',
                        'Trust (Government Corruption)':'Tr',
                       'Generosity':'Gn','Dystopia Residual':'DR'},
                           axis=1)

var_2015 = var_2015.corr()
sns.heatmap(var_2015,square=True)
plt.show()
