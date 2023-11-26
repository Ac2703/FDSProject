import pandas as pd
import numpy as np

# Returns: input DF without outliers
def removeOutliersIQR(df, col):
    colValList = list(df[col])
    q1 = np.quantile(colValList, 0.25)
    q3 = np.quantile(colValList, 0.75)
    iqr = q3 - q1
    prod = iqr * 1.5
    outlierList = []
    for item in colValList:
        # if (item > Q3 + IQR * 1.5) or (item < Q1 - IQR * 1.5)
        if (item > (q3 + prod)) or (item < (q1 - prod)):
            # print item
            outlierList.append(item)
            df = df.drop(df[df[col] == item].index)
    return df


# CLEANING MANU DF
def manu_process(ManuDF):
    ManuDF = ManuDF.drop('Condo_Project', axis=1) # drop Condo_Project (100% missing)
    ManuDF = ManuDF.drop('Room_Count', axis=1) # drop Room_Num (100% missing)
    ManuDF = ManuDF.drop('Bdrm_Count', axis=1) # drop Bdrm_Num (100% missing)
    ManuDF = ManuDF.drop('Ext_Wall', axis=1) # drop Ext_Wall (50% missing)
    ManuDF = ManuDF.drop('Story_Count', axis=1) # drop Story_Num (50% missing)
    ManuDF = ManuDF.drop('Year_Built', axis=1) # drop Year_Built (50% missing)
    ManuDF = ManuDF.drop('Finished_Sqft', axis=1) # drop Finished_Sqft (33.3% missing)
    return ManuDF

# CLEANING COMM DF
def comm_process(CommDF):
    CommDF = CommDF.drop('Condo_Project', axis=1) # drop Condo_Project (100% missing)
    CommDF['Room_Count'] = CommDF['Room_Count'].fillna(CommDF['Room_Count'].median())
    CommDF['Finished_Sqft'] = CommDF['Finished_Sqft'].fillna(CommDF['Finished_Sqft'].median())
    CommDF['Bdrm_Count'] = CommDF['Bdrm_Count'].fillna(CommDF['Bdrm_Count'].median())
    CommDF['Unit_Count'] = CommDF['Unit_Count'].fillna(CommDF['Unit_Count'].median())
    CommDF['Lot_Size'] = CommDF['Lot_Size'].fillna(CommDF['Lot_Size'].median())

    CommDF = removeOutliersIQR(CommDF,'Room_Count')
    CommDF = removeOutliersIQR(CommDF,'Finished_Sqft')
    CommDF = removeOutliersIQR(CommDF,'Bdrm_Count')
    CommDF = removeOutliersIQR(CommDF,'Unit_Count')
    CommDF = removeOutliersIQR(CommDF,'Lot_Size')
    
    return CommDF

# CLEANING RES DF
def res_process(ResDF):
    ResDF = ResDF.drop('Condo_Project', axis=1) # drop Condo_Project (100% missing)
    ResDF = ResDF.drop(ResDF.loc[ResDF['Lot_Size']==0].index) # TEMPORARY: drop instance swith 0 lotsize

    ResDF['Room_Count'] = ResDF['Room_Count'].fillna(ResDF['Room_Count'].median())
    ResDF['Finished_Sqft'] = ResDF['Finished_Sqft'].fillna(ResDF['Finished_Sqft'].median())
    ResDF['Bdrm_Count'] = ResDF['Bdrm_Count'].fillna(ResDF['Bdrm_Count'].median())
    ResDF['Lot_Size'] = ResDF['Lot_Size'].fillna(ResDF['Lot_Size'].median())

    ResDF = removeOutliersIQR(ResDF,'Room_Count')
    ResDF = removeOutliersIQR(ResDF,'Finished_Sqft')
    ResDF = removeOutliersIQR(ResDF,'Bdrm_Count')
    ResDF = removeOutliersIQR(ResDF,'Lot_Size')

    return ResDF

# CLEANING CONDO DF
def condo_process(CondoDF):
    CondoDF = CondoDF.drop('Ext_Wall', axis=1) # drop Ext_Wall (100% missing)

    CondoDF['Story_Count'] = CondoDF['Story_Count'].fillna(CondoDF['Story_Count'].median())
    CondoDF['Room_Count'] = CondoDF['Room_Count'].fillna(CondoDF['Room_Count'].median())
    CondoDF['Bdrm_Count'] = CondoDF['Bdrm_Count'].fillna(CondoDF['Bdrm_Count'].median())

    CondoDF = removeOutliersIQR(CondoDF,'Room_Count')
    CondoDF = removeOutliersIQR(CondoDF,'Finished_Sqft')
    CondoDF = removeOutliersIQR(CondoDF,'Bdrm_Count')
    CondoDF = removeOutliersIQR(CondoDF,'Unit_Count')

    return CondoDF

# CLEANING APT DF
def apt_process(AptDF):
    AptDF = AptDF.drop('Condo_Project', axis=1) # drop Condo_Project (100% missing)
    AptDF = AptDF.drop('Room_Count', axis=1) # drop Room_Count (100% missing)
    AptDF = AptDF.drop('Bdrm_Count', axis=1) # drop Bdrm_Count (100% missing)

    #AptDF = removeOutliersIQR(AptDF,'Room_Count')
    #AptDF = removeOutliersIQR(AptDF,'Bdrm_Count')
    AptDF = removeOutliersIQR(AptDF,'Finished_Sqft')
    AptDF = removeOutliersIQR(AptDF,'Unit_Count')

    return AptDF

# CLEANING EXEMPT DF
def exempt_process(ExemptDF):
    ExemptDF = ExemptDF.drop('Condo_Project', axis=1) # drop Condo_Project (100% missing)
    return ExemptDF

