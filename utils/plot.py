## Common Functions

#%matplotlib inline

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils.constants import FIG_SIZE,FONT_SIZE,CMAP_RAINBOW

__all__ = ["histogram","scatter","pair"]


# RC Params for seaborn
plt.rcParams['figure.figsize'] = FIG_SIZE  # Set default figure size
#plt.rcParams['font.family'] = 'calibri'    # Set default font family
plt.rcParams['font.size'] = FONT_SIZE          # Set default font size
plt.rcParams['lines.linewidth'] = 2      # Set default line width
#plt.rcParams['style'] == plt_style

def histogram(data, x, xtitle=None):
    if xtitle is None:
        xtitle = x
    fig, ax = plt.subplots()
    #plt_style
    sns.histplot(data = data, x=x, ax=ax)
    ax.set_title(f"Frequency of {xtitle}")
    ax.set_xlabel(xtitle)
    ax.set_ylabel('Frequency')
    plt.show()
    
def scatter(data ,x, y, hue=None, xtitle=None, ytitle=None):
    if xtitle is None:
        xtitle = x
    if ytitle is None:
        ytitle = y
    fig, ax = plt.subplots()
    if hue is None:
        print("Hue is : None ", hue)
        sns.scatterplot(data = data, x = x, y = y, ax= ax)
    else: 
        print("Hue is : not None ", hue)
        sns.scatterplot(data = data, x = x, y = y, hue = hue,palette=CMAP_RAINBOW, ax= ax)
    #(lambda hue=hue: {'hue': hue, 'palette': 'rainbow'} if hue else {})(hue)
    ax.set_title(f"Plot of {xtitle} vs {ytitle}")
    ax.set_xlabel(xtitle)
    ax.set_ylabel(ytitle)
    plt.show()

def countplot(data, x, xtitle=None):
    if xtitle is None:
        xtitle = x
    fig, ax = plt.subplots()
    sns.countplot(x=x, data=data, palette=CMAP_RAINBOW, order = data[x].value_counts().index)
    # Rotate the x labels by 90 degrees and hide the extra text
    _ = plt.xticks(rotation=90)
    ax.set_title(f"Count of {xtitle}")
    ax.set_xlabel(xtitle)
    ax.set_ylabel("Count")

def pair():
    pass 


def visualise_evaluation_metrics():
    pass