## Common Functions

#%matplotlib inline

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils.constants import FIG_SIZE,FONT_SIZE

__all__ =["histogram","scatter","pair"]


# RC Params for seaborn
plt.rcParams['figure.figsize'] = FIG_SIZE  # Set default figure size
plt.rcParams['font.family'] = 'serif'    # Set default font family
plt.rcParams['font.size'] = FONT_SIZE          # Set default font size
plt.rcParams['lines.linewidth'] = 2      # Set default line width
#plt.rcParams['style'] == plt_style

def histogram(data, x, xtitle):
    fig, ax = plt.subplots()
    #plt_style
    sns.histplot(data = data, x=x, ax=ax)
    ax.set_title(f"Frequency of {xtitle}")
    ax.set_xlabel(xtitle)
    ax.set_ylabel('Frequency')
    plt.show()
    
def scatter(data ,x, y, xtitle, ytitle, hue):
    fig, ax = plt.subplots()
    #plt_style
    sns.scatterplot(data = data, x = x, y = y, hue = hue, palette=constants.CMAP_RAINBOW, ax= ax)
    #(lambda hue=hue: {'hue': hue, 'palette': 'rainbow'} if hue else {})(hue)
    ax.set_title(f"Plot of {xtitle} vs {ytitle}")
    ax.set_xlabel(xtitle)
    ax.set_ylabel(ytitle)
    plt.show()

def pair():
    pass 


def visualise_evaluation_metrics():
    pass