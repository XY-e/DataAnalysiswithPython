import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Load the dataset
    df = pd.read_csv('epa-sea-level.csv')

    # Create a scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', s=10, label='Data')

    # Fit line to the entire dataset
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = pd.Series(range(df['Year'].min(), 2051))
    line = slope * years + intercept
    plt.plot(years, line, color='red', linestyle='--', label='Fit Line (All Data)')

    # Fit line to the data from 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    line_recent = slope_recent * years + intercept_recent
    plt.plot(years, line_recent, color='green', linestyle='--', label='Fit Line (2000 onwards)')

    # Set labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save and show the plot
    plt.savefig('sea_level_plot.png')
    plt.show()
    return plt.gcf()
