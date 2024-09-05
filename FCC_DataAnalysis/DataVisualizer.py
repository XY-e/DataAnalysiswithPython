import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def draw_cat_plot():
    # Load the dataset
    df = pd.read_csv('medical_examination.csv')
    
    # Calculate BMI and create the overweight column
    df['bmi'] = df['weight'] / (df['height'] / 100) ** 2
    df['overweight'] = (df['bmi'] > 25).astype(int)
    
    # Normalize cholesterol and glucose
    df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
    df['gluc'] = (df['gluc'] > 1).astype(int)
    
    # Convert data into long format
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    # Group and reformat the data
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    # Create the catplot
    fig = sns.catplot(x='variable', hue='value', col='cardio', data=df_cat, kind='bar', height=5, aspect=1.2)
    plt.show()
    return fig

def draw_heat_map():
    # Load the dataset
    df = pd.read_csv('medical_examination.csv')
    
    # Calculate BMI and create the overweight column
    df['bmi'] = df['weight'] / (df['height'] / 100) ** 2
    df['overweight'] = (df['bmi'] > 25).astype(int)
    
    # Normalize cholesterol and glucose
    df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
    df['gluc'] = (df['gluc'] > 1).astype(int)
    
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]
    
    # Calculate the correlation matrix
    corr = df_heat.corr()
    
    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # Set up the matplotlib figure
    plt.figure(figsize=(10, 8))
    
    # Plot the heatmap
    fig = sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", cmap='coolwarm', center=0)
    plt.show()
    return fig

