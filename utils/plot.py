## Common Functions

#%matplotlib inline

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
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
        xtitle = x.capitalize()
    fig, ax = plt.subplots()
    #plt_style
    sns.histplot(data = data, x=x, ax=ax)
    ax.set_title(f"Frequency of {xtitle}")
    ax.set_xlabel(xtitle)
    ax.set_ylabel('Frequency')
    if data[x].nunique()>10:
        _ = plt.xticks(rotation=90)
    
    plt.show()
    
def scatter(data ,x, y, hue=None, xtitle=None, ytitle=None):
    if xtitle is None:
        xtitle = x.capitalize()
    if ytitle is None:
        ytitle = y.capitalize()
    fig, ax = plt.subplots()
    if hue is None:
        sns.scatterplot(data = data, x = x, y = y, ax= ax)
    else: 
        sns.scatterplot(data = data, x = x, y = y, hue = hue,palette=CMAP_RAINBOW, ax= ax)
    #(lambda hue=hue: {'hue': hue, 'palette': 'rainbow'} if hue else {})(hue)
    ax.set_title(f"Plot of {xtitle} vs {ytitle}")
    ax.set_xlabel(xtitle)
    ax.set_ylabel(ytitle)
    plt.show()

def countplot(data, x, xtitle=None):
    if xtitle is None:
        xtitle = x.capitalize()
    fig, ax = plt.subplots()
    sns.countplot(x=x, data=data, palette=CMAP_RAINBOW, order = data[x].value_counts().index)
    # Rotate the x labels by 90 degrees and hide the extra text
    if data[x].nunique()>10:
        _ = plt.xticks(rotation=90)
    ax.set_title(f"Count of {xtitle}")
    ax.set_xlabel(xtitle)
    ax.set_ylabel("Count")

def pair():
    pass 


def visualise_evaluation_metrics():
    pass

def bar_count_percent(data, x, y, xtitle=None, ytitle =None):
    if xtitle is None:
        xtitle = x.capitalize()
    if ytitle is None:
        ytitle = y.capitalize()
    # Group by Country and State
    grouped = data.groupby([x, y]).size().unstack(fill_value=0)

    grouped['Total'] = grouped.sum(axis=1)
    grouped['Success Rate'] = grouped['Successful'] / grouped['Total']
    print(grouped)

    # Fill missing 'Successful' or 'Non-Successful' with 0
    grouped = grouped.fillna(0)

    # Sort by total count in descending order
    grouped = grouped.sort_values(by='Total', ascending=False)

    grouped_reset = grouped.reset_index()

    fig, axes = plt.subplots(2, 1, figsize=(14, 12))

    # Total counts subplot
    sns.barplot(data=grouped_reset, x=x, y='Total', ax=axes[0])
    axes[0].set_title(f'Total Count of Successful vs. Non-Successful by {x}')
    axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=90)
    # Success rate by Country
    sns.barplot(data=grouped_reset, x=x, y='Success Rate', ax=axes[1])
    axes[1].set_title('Success Rate by {x}')
    axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=90)


    plt.tight_layout()
    plt.show()