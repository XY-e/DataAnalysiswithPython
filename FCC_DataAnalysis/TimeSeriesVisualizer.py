import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def draw_line_plot():
    # Load and clean the dataset
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
    q_low = df['value'].quantile(0.025)
    q_high = df['value'].quantile(0.975)
    df_clean = df[(df['value'] >= q_low) & (df['value'] <= q_high)]
    
    # Create a copy of the cleaned data
    df_line = df_clean.copy()
    
    # Plot the line chart
    plt.figure(figsize=(12, 6))
    plt.plot(df_line.index, df_line['value'], color='blue')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.grid(True)
    
    # Save and return the figure
    plt.savefig('line_plot.png')
    plt.show()
    return plt.gcf()

def draw_bar_plot():
    # Load and clean the dataset
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
    q_low = df['value'].quantile(0.025)
    q_high = df['value'].quantile(0.975)
    df_clean = df[(df['value'] >= q_low) & (df['value'] <= q_high)]
    
    # Create a copy of the cleaned data
    df_bar = df_clean.copy()
    
    # Extract year and month from the date
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    
    # Group by year and month and calculate the average
    df_bar_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    
    # Plot the bar chart
    plt.figure(figsize=(12, 6))
    df_bar_grouped.plot(kind='bar', figsize=(12, 6))
    plt.title('Average Page Views per Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    
    # Save and return the figure
    plt.savefig('bar_plot.png')
    plt.show()
    return plt.gcf()

def draw_box_plot():
    # Load and clean the dataset
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
    q_low = df['value'].quantile(0.025)
    q_high = df['value'].quantile(0.975)
    df_clean = df[(df['value'] >= q_low) & (df['value'] <= q_high)]
    
    # Create a copy of the cleaned data
    df_box = df_clean.copy()
    
    # Extract year and month from the date
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.month
    
    # Prepare data for the box plots
    df_box['month'] = df_box['month'].apply(lambda x: pd.to_datetime(str(x), format='%m').strftime('%b'))
    
    # Create the year-wise box plot
    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    sns.boxplot(x='year', y='value', data=df_box)
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    
    # Create the month-wise box plot
    plt.subplot(1, 2, 2)
    sns.boxplot(x='month', y='value', data=df_box, order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    
    # Save and return the figure
    plt.savefig('box_plot.png')
    plt.show()
    return plt.gcf()
