import pandas as pd
from processing import *
from visualizing import * 

# Returns: DFs of each subset of Property Type
def split_data(mainDF): 
    ManuDF = mainDF[mainDF['Prop_Type'] == 'Manufacturing'] # Manufacturing
    CommDF = mainDF[mainDF['Prop_Type'] == 'Commercial'] # Commercial
    ResDF = mainDF[mainDF['Prop_Type'] == 'Residential'] # Residential
    CondoDF = mainDF[mainDF['Prop_Type'] == 'Condominium'] # CondoDF
    AptDF = mainDF[mainDF['Prop_Type'] == 'Lg Apartment'] # Lg Apt DF
    ExemptDF = mainDF[mainDF['Prop_Type'] == 'Exempt'] #ExemptDF
    return (ManuDF, CommDF, ResDF, CondoDF, AptDF, ExemptDF)

# Returns: percentage of missing values in each column
def missingValAmt(df):
    missingDF = df.isna() # turn main DF into T/F for Missing/Not Missing
    missingNum = missingDF.sum() # sums each column in the missing DF
    missingNumPerc = (missingNum / len(df)) * 100 # prints percentage of missing values in each column
    return(missingNumPerc, missingNum)

# Returns: a DF of statistics for each column
def showStatistics(df):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  
        statDF = df.describe(include='all').T
        statDF = df.to_string()
    return(statDF)

# Prints: all the subset DFs
def printSplitDFs(ManuDF, CommDF, ResDF, CondoDF, AptDF, ExemptDF):
    print(" ")
    print("#---Manufacturing---#")
    print(ManuDF)
    print(" ")

    print("#---Commerical---#")
    print(CommDF)
    print(" ")

    print("#---Residential---#")
    print(ResDF)
    print(" ")

    print("#---Condominium---#")
    print(CondoDF)
    print(" ")

    print("#---Apartment---#")
    print(AptDF)
    print(" ")

    print("#---Exempt---#")
    print(ExemptDF)
    print(" ")

# Returns: list of outliers
def showOutliersIQR(df,col):
    colValList = sorted(list(df[col]))
    q1 = np.quantile(colValList, 0.25)
    print(q1)
    q3 = np.quantile(colValList, 0.75)
    print(q3)
    iqr = q3 - q1
    print(iqr)
    prod = iqr * 1.5
    outlierList = []
    for item in colValList:
        # if (item > Q3 + IQR * 1.5) or (item < Q1 - IQR * 1.5)
        if (item > (q3 + prod)):
            # print item
            outlierList.append(item)
        elif (item < (q1 - prod)):
            outlierList.append(item)
    
    return sorted(outlierList)

def corrMatrix(ManuDF, CommDF, ResDF, CondoDF, AptDF, ExemptDF):
    corrManu = ManuDF[ManuDF.columns[1:]].corr()['Sale_Price'][:-1]
    corrComm = CommDF[CommDF.columns[1:]].corr()['Sale_Price'][:-1]
    corrRes = ResDF[ResDF.columns[1:]].corr()['Sale_Price'][:-1]
    corrCondo = CondoDF[CondoDF.columns[1:]].corr()['Sale_Price'][:-1]
    corrApt = AptDF[AptDF.columns[1:]].corr()['Sale_Price'][:-1]
    corrExempt = ExemptDF[ExemptDF.columns[1:]].corr()['Sale_Price'][:-1]
    corrDF = pd.DataFrame({'Manu' : pd.Series(corrManu), 'Comm' : pd.Series(corrComm), 'Res' : pd.Series(corrRes), 'Condo' : pd.Series(corrCondo), 'Apt' : pd.Series(corrApt), 'Exempt' : pd.Series(corrExempt)})
    return corrDF

def main():
    print("     ")
    pd.set_option('display.max_columns', None)

    # ---- SET UP DATAFRAME ---- #
    file = pd.read_csv("DATA/2022-property-sales-data.csv")
    ogDF = pd.DataFrame(file)
    mainDF = pd.DataFrame(file)
    mainDF.rename(columns={'PropertyID': 'Property_ID', 'PropType': 'Prop_Type', 'taxkey': 'Tax_Key', 'Address': 'Address', 'CondoProject':'Condo_Project', 'District': 'District_Num', 'nbhd':'Nbhd_Num', 'Style':'Style', 'Extwall':'Ext_Wall', 'Stories':'Story_Count', 'Year_Built':'Year_Built', 'Rooms': 'Room_Count', 'FinishedSqft' : 'Finished_Sqft', 'Units' : 'Unit_Count', 'Bdrms' : 'Bdrm_Count', 'Fbath' : 'Fbath_Count', 'Hbath' : 'Hbath_Count', 'Lotsize' : 'Lot_Size', 'Sale_date' : 'Sale_Date', 'Sale_price' : 'Sale_Price'}, inplace=True)

    # ---- CLEAN MAIN DF ---- #
    mainDF = mainDF.drop(mainDF.loc[mainDF['Year_Built']==0].index) # 
    #mainDF = mainDF.drop(mainDF.loc[mainDF['Lot_Size']==0].index)

    # ---- SPLIT DATAFRAMES ---- #
    ManuDF, CommDF, ResDF, CondoDF, AptDF, ExemptDF = split_data(mainDF)
    #printSplitDFs(ManuDF, CommDF, ResDF, CondoDF, AptDF, ExemptDF)
    
    # ---- VISUALIZE BEFORE CLEANING ---- #
    #vis_sns_SPLOM(AptDF, 'VIS/EXEMPT/exempt_splom_raw.png')

    # ---- CLEAN SUBSET DFs ---- #
    ManuDF = manu_process(ManuDF)
    CommDF = comm_process(CommDF)
    ResDF = res_process(ResDF)
    CondoDF = condo_process(CondoDF)
    AptDF = apt_process(AptDF)
    ExemptDF = exempt_process(ExemptDF)

    # ---- STATISTICS FOR SUBSET DFs ---- #
    #print(showStatistics(mainDF))
    #print(corrMatrix(ManuDF, CommDF, ResDF, CondoDF, AptDF, ExemptDF))

    # ---- VISUALIZE ---- #

    # -- MAIN
    #vis_sns_SPLOM(mainDF, 'VIS/MAIN/main_splom_fixed.png') # MainDF Correlations - SPLOM 
    #vis_HIST(mainDF, 'Sale_Price', 'VIS/MAIN/main_sale_dist.png') # MainDF SalePrice Distribution - HISTOGRAM
    #vis_LINEPLOT(mainDF, 'Year_Built', 'Sale_Price', 'VIS/MAIN/main_year_vs_price_line.png') # MainDF YearBuilt vs SalePrice - LINEPLOT

    # -- MANU
    #vis_sns_SPLOM(ManuDF, 'VIS/MANU/manu_splom_fixed.png') # ManuDF Correlations - SPLOM

    # -- COMM
    #vis_sns_SPLOM(CommDF, 'VIS/COMM/comm_splom_fixed.png') # CommDF Correlations - SPLOM

    # -- RES
    #vis_sns_SPLOM(ResDF, 'VIS/RES/res_splom_fixed.png') # ResDF Correlations - SPLOM
    #vis_LINEPLOT(ResDF, 'Finished_Sqft', 'Sale_Price', 'VIS/RES/res_sqft_vs_price_line.png') # ResDF FinishedSqft vs SalePrice - LINEPLOT
    #vis_HIST(ResDF, 'Room_Count', 'VIS/RES/res_room_dist_fixed.png')  #ResDF Room Distribution - HISTOGRAM

    # -- CONDO
    #vis_sns_SPLOM(CondoDF, 'VIS/CONDO/condo_splom_fixed.png') # CondoDF Correlations - SPLOM

    # -- APT
    #vis_sns_SPLOM(AptDF, 'VIS/APT/apt_splom_fixed.png') # AptDF Correlations - SPLOM

    # -- EXEMPT 
    #vis_sns_SPLOM(AptDF, 'VIS/EXEMPT/exempt_splom_fixed.png')

    # ---- TEST ---- #

    # ---- UPDATE CSV ---- #
    while True:
        try:
            ManuDF.to_csv('DATA/CLEANED_2022_Property_Sales.csv', mode ='x', sep=',')
            CommDF.to_csv('DATA/CLEANED_2022_Property_Sales.csv', mode ='a', sep=',')
            ResDF.to_csv('DATA/CLEANED_2022_Property_Sales.csv', mode ='a', sep=',')
            CondoDF.to_csv('DATA/CLEANED_2022_Property_Sales.csv', mode ='a', sep=',')
            AptDF.to_csv('DATA/CLEANED_2022_Property_Sales.csv', mode ='a', sep=',')
            ExemptDF.to_csv('DATA/CLEANED_2022_Property_Sales.csv', mode ='a', sep=',')
        except:
            print(" ")
            print("There was an error updating the CSV file.")
        else:
            print(" ")
            print("Successfully updated CSV file!")
            break

if __name__ == '__main__':
    main()