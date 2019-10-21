import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# --------------------------------------------------------------------------------------------

var_2015 = pd.read_csv(r'D:\Projects\SDL_WHR\2015.csv',index_col = "Country")
var_2015 = pd.DataFrame(var_2015)
var_2015 = var_2015.rename({'Country': 'C',
                            'Region': 'R',
                            'Happiness Rank': 'HR',
                            'Happiness Score': 'HS',
                            'Standard Error':'SE',
                            'Economy (GDP per Capita)':'EC',
                            'Family':'FA',
                            'Health (Life Expectancy)':'HE',
                            'Freedom':'FR',
                            'Trust (Government Corruption)':'TR',
                            'Generosity':'GN',
                            'Dystopia Residual':'DR'},
                            axis=1)

# --------------------------------------------------------------------------------------------

var_2016 = pd.read_csv(r'D:\Projects\SDL_WHR\2016.csv',index_col = "Country")
var_2016 = pd.DataFrame(var_2016)
var_2016 = var_2016.rename({'Country': 'C',
                            'Region': 'R',
                            'Happiness Rank': 'HR',
                            'Happiness Score': 'HS',
                            'Lower Confidence Interval':'LCI',
                            'Upper Confidence Interval':'UCI',
                            'Economy (GDP per Capita)':'EC',
                            'Family':'FA',
                            'Health (Life Expectancy)':'HE',
                            'Freedom':'FR',
                            'Trust (Government Corruption)':'TR',
                            'Generosity':'GN',
                            'Dystopia Residual':'DR'},
                            axis=1)

# --------------------------------------------------------------------------------------------

var_2017 = pd.read_csv(r'D:\Projects\SDL_WHR\2017.csv',index_col = "Country")
var_2017 = pd.DataFrame(var_2017)
var_2017 = var_2017.rename({'Country': 'C',
                            'Happiness.Rank': 'HR',
                            'Happiness.Score': 'HS',
                            'Whisker.high':'WH',
                            'Whisker.low':'WL',
                            'Economy..GDP.per.Capita.':'EC',
                            'Family':'FA',
                            'Health..Life.Expectancy.':'HE',
                            'Freedom':'FR',
                            'Trust..Government.Corruption.':'TR',
                            'Generosity':'GN',
                            'Dystopia.Residual':'DR'},
                           axis=1)
# --------------------------------------------------------------------------------------------

desc_2015 = var_2015.describe()
desc_2016 = var_2016.describe()
desc_2017 = var_2017.describe()

# --------------------------------------------------------------------------------------------

