import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
   PATH='https://raw.githubusercontent.com/freeCodeCamp/boilerplate-sea-level-predictor/master/epa-sea-level.csv'
   df = pd.read_csv(PATH)

    # Read data from file
    PATH='https://raw.githubusercontent.com/freeCodeCamp/boilerplate-sea-level-predictor/master/epa-sea-level.csv'
    df = pd.read_csv(PATH)

    # Create scatter plot
    fig, ax = plt.subplots()
    ax = plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    # Create first line of best fit
    lin = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    ax=plt.plot(df['Year'], lin.slope*df['Year'] + lin.intercept)
    # Create second line of best fit
    ax=plt.plot(np.arange(2000,2050), lin.slope*np.arange(2000,2050) + lin.intercept)

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()