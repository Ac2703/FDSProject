import pandas as pd
import numpy as np

# ---- SET UP DATAFRAME ---- #
file = pd.read_csv("2022-property-sales-data.csv")
ogDF = pd.DataFrame(file)
mainDF = pd.DataFrame(file)


# ---- FIND UNIQUE VALUES ---- #
columnList = list(mainDF.columns.values)
propType_unique = list(mainDF['PropType'].unique())
district_unique = list(mainDF['District'].unique())
extWall_unique = list(mainDF['Extwall'].unique())


# ---- FIND % OF MISSING VALUES ---- #
missingDF = mainDF.isna() # turn main DF into T/F for Missing/Not Mising
missingDF.dtypes # verify that it's all booleans
missingNum = missingDF.sum() # sums each column in the missing DF
missingNumPerc = (missingNum / len(mainDF)) * 100 # prints percentage of missing values in each column


# ---- FIND STATISTICS ---- #
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  
    statDF = mainDF.describe(include='all').T
    statDF = statDF.to_string()

# ----- ADD SALE MONTH COLUMN ---- #
saleDateList = list(mainDF['Sale_date'])
saleMonthList = []
for date in saleDateList:
    saleMonthList.append(date[5:7])
saleMonthList.sort()
mainDF['Sale_Month'] = saleMonthList
saleMonth_unique = mainDF['Sale_Month'].unique()


# ----- CLEANING DATA ---- #
mainDF = mainDF.drop('CondoProject', axis='columns')

# ---- UPDATE CSV ---- #
while True:
    try:
        mainDF.to_csv('CLEANED_2022_Property_Sales.csv', mode ='w', sep=',')
    except:
        print("There was an error updating the CSV file.")
    else:
        print("Successfully updated CSV file!")
        break

def main():
    print(" ")
    print("--- OG DATAFRAME ---")
    print(ogDF)

    print(" ")
    print("--- BASIC INFO ---")
    mainDF.info()

    print(" ")
    print("--- UNIQUE VALUES ---")
    print(propType_unique)
    print(district_unique)
    print(extWall_unique)

    print(" ")
    print("--- MISSING % ---")
    print(missingNumPerc)

    print(" ")
    print("--- STATISTICS ---")
    print(statDF)

    print(" ")
    print("--- SALE MONTH COLUMN ---")
    print(saleMonth_unique)

    print(" ")
    print("--- MAIN DATAFRAME ---")
    print(mainDF)



   

if __name__ == '__main__':
    main()
