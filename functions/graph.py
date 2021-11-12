
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def heatmap_grafica(df, xlabel, ylabel, title):
    plt.figure(figsize=(18,8))
    ax = sns.heatmap(df, cmap='YlGnBu')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation=90)
    plt.yticks(rotation=0)
    plt.show()

