import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def vis_plt_SPLOM(df, xcol, ycol, path):
    xval = list(df[xcol])
    yval = list(df[ycol])

    plt.scatter(xval, yval)
    plt.savefig(path)
    plt.close()

def vis_sns_SPLOM(df, path):
    sns_splom = sns.pairplot(df)
    sns_splom.savefig(path)
    plt.close()

def vis_HIST(df, col, path):
    sns.histplot(df[col], kde=True, color="m")
    plt.savefig(path)
    plt.clf()

def vis_LINEPLOT(df, xval, yval, path):
    sns.lineplot(x = xval, y = yval, data = df)
    plt.savefig(path)
    plt.clf()

def vis_BOXPLOT(x):
    pass

