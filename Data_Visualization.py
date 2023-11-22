import matplotlib.pyplot as plt
import pandas as pd
import data_processing as data_proc
import scipy as sp


file = pd.read_csv("CLEANED_2022_Property_Sales.csv")

mainDF = data_proc.mainDF

# ---- MONTH VS SALES PRICE---- #
ypoints = scipy.stats.binned_statistic_mainDF['Sale_price']
plt.scatter(mainDF['Sale_Month'].unique(), mainDF['Sale_price'])

plt.show()
