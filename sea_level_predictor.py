import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress



def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(16, 9))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    result = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    start_year = df["Year"].min()
    end_year = 2050
    
    x_values = range(start_year, end_year + 1)
    y_values = [result.slope * year + result.intercept for year in x_values]
    
    plt.plot(x_values, y_values, 'r')

    # Create second line of best fit
    start_year = 2000
    df_recent = df[df["Year"] >= start_year]
    result_recent = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    
    x_values_recent = range(start_year, end_year + 1)
    y_values_recent = [result_recent.slope * year + result_recent.intercept for year in x_values_recent]
    
    plt.plot(x_values_recent, y_values_recent, 'g')

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

"""
def draw_plot():
    # Read data from file


    # Create scatter plot


    # Create first line of best fit


    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
    """
