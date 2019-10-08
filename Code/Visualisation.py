import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

desired_width = 320
pd.set_option("display.width",desired_width)
pd.set_option("display.max_columns",20)
pd.set_option("display.max_rows",200)

#---------------------------------------------------------------------------------------------------------------

var_2015 = pd.read_csv(r'D:\Projects\SDL_WHR\2015.csv',index_col="Country")
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

#---------------------------------------------------------------------------------------------------------------

var_2016 = pd.read_csv(r'D:\Projects\SDL_WHR\2016.csv',index_col="Country")
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
#---------------------------------------------------------------------------------------------------------------
var_2017 = pd.read_csv(r'D:\Projects\SDL_WHR\2017.csv',index_col="Country")
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
#---------------------------------------------------------------------------------------------------------------

desc_2015 = var_2015.describe()
desc_2016 = var_2016.describe()
desc_2017 = var_2017.describe()

# def graph_meanhs():
#     plt.rcParams['figure.figsize'] = [7,7]
#     x = ['2015','2016','2017']
#     y1 = desc_2015['HS']['mean']
#     y2 = desc_2016['HS']['mean']
#     y3 = desc_2017['HS']['mean']
#     y = [y1,y2,y3]
#     plt.plot(x,y,linestyle = '-',marker = 'o', color = 'g')
#     plt.xlabel("Year")
#     plt.ylabel("Mean Happiness Score")
#     plt.title("Mean Happiness vs Year")
#     plt.show()
#
# def graph_maxmin():
#     plt.rcParams['figure.figsize'] = [7, 7]
#
#     x = ['2015', '2016', '2017']
#     ymax1 = desc_2015['HS']['max']
#     ymax2 = desc_2016['HS']['max']
#     ymax3 = desc_2017['HS']['max']
#     ymax = [ymax1, ymax2, ymax3]
#
#     ymin1 = desc_2015['HS']['min']
#     ymin2 = desc_2016['HS']['min']
#     ymin3 = desc_2017['HS']['min']
#     ymin = [ymin1, ymin2, ymin3]
#
#     plt.plot(x, ymax, linestyle='-', marker='o', color='b', label='Maximum HS')
#     plt.plot(x, ymin, linestyle='-', marker='o', color='r', label='Minimum HS')
#
#     for i, j in zip(x, ymax):
#         plt.annotate(str(j), xy=(i, j), xytext=(-15, -15), textcoords='offset points')
#
#     for i, j in zip(x, ymin):
#         plt.annotate(str(j), xy=(i, j), xytext=(2, 15), textcoords='offset points')
#
#     plt.xlabel("Year")
#     plt.ylabel("Happiness Score")
#     plt.title('Max/Min Happiness Scores Yearwise')
#     plt.legend()
#     plt.show()
#
# def countryfn():
#     f = input("Enter the name of the country : ")
#
#     plt.rcParams['figure.figsize'] = [10, 10]
#
#     c1 = var_2015.loc[f]
#     c2 = var_2016.loc[f]
#     c3 = var_2017.loc[f]
#
#     leg = ['Economy', 'Family', 'Health', 'Freedom', 'Trust', 'Generosity']
#
#     c1 = [c1['HR'], c1['EC'], c1['FA'], c1['HE'], c1['FR'], c1['TR'], c1['GN']]
#     c2 = [c2['HR'], c2['EC'], c2['FA'], c2['HE'], c2['FR'], c2['TR'], c2['GN']]
#     c3 = [c3['HR'], c3['EC'], c3['FA'], c3['HE'], c3['FR'], c3['TR'], c3['GN']]
#
#     for i in range(1, 6):
#         plt.plot(['2015', '2016', '2017'], [c1[i], c2[i], c3[i]], marker='o', label=leg[i])
#
#     plt.title('Country level analysis')
#     plt.xlabel('Year')
#     plt.ylabel('Units')
#     plt.legend()
#     plt.show()
#
# def comparisionfn():
#     import matplotlib.pyplot as plt
#     f1 = input("Enter the 1st Country : ")
#     f2 = input("Enter the 2nd Country : ")
#     f = [f1, f2]
#
#     plt.rcParams['figure.figsize'] = [15, 10]
#     fig, axs = plt.subplots(1, 2)
#
#     for j in range(2):
#         c1 = var_2015.loc[f[j]]
#         c2 = var_2016.loc[f[j]]
#         c3 = var_2017.loc[f[j]]
#
#         leg = ['Economy', 'Family', 'Health', 'Freedom', 'Trust', 'Generosity']
#
#         c1 = [c1['HR'], c1['EC'], c1['FA'], c1['HE'], c1['FR'], c1['TR'], c1['GN']]
#         c2 = [c2['HR'], c2['EC'], c2['FA'], c2['HE'], c2['FR'], c2['TR'], c2['GN']]
#         c3 = [c3['HR'], c3['EC'], c3['FA'], c3['HE'], c3['FR'], c3['TR'], c3['GN']]
#
#         for i in range(1, 6):
#             axs[j].plot(['2015', '2016', '2017'], [c1[i], c2[i], c3[i]], marker='o', label=leg[i])
#
#         axs[j].set_title("%s" % f[j])
#     for axs in axs.flat:
#         axs.set(xlabel='Years', ylabel='Units')
#         axs.legend()
#     plt.show()

# def scatterfn():
#     import matplotlib.pyplot as plt
#     features = ['HS', 'EC', 'FA', 'HE', 'FR', 'TR', 'GN']
#     desc_list = ["Happiness Score","Economy","Family","Health","Freedom","Trust on Government","Generosity"]
#     choice1 = int(input("Enter the 1st Feature : "))
#     choice2 = int(input("Enter the 2nd Feature : "))
#
#     plt.scatter(var_2015[features[choice1]], var_2015[features[choice2]])
#
#     plt.xlabel("%s" % desc_list[choice1])
#     plt.ylabel("%s" % desc_list[choice2])
#     plt.title("%s VS %s" % (features[choice1], features[choice2]))
#     plt.show()
#
# scatterfn()
