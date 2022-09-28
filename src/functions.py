import pandas as pd
import matplotlib.pyplot as plt

def plot_hist(data, col, title, xlabel):
    
    '''Summary Line
    
    More detailed description (optional, only for complex functions)
    
    Parameters
    
    Returns
    
    '''
    
    fig, ax = plt.subplots(figsize=(10,6))
    ax.hist(data[col])
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    plt.show()


def plot_hist(data, col, title, xlabel):
    
    '''Plots histogram of continuous data
    
    Function accepts data, column to be plotted, title and label.
    Plots detailed histogram of data.
    
    Parameters
    ----------
    data : pandas DataFrame
        DataFrame containing column to be visualized
    col : str
        column in DataFrame to plot
    title : str
        title of histogram
    xlabel : str
        label for x-axis on histogram
    
    '''
    
    fig, ax = plt.subplots(figsize=(10,6))
    ax.hist(data[col])
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    plt.show()
    
    
    
    