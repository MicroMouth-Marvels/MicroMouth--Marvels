#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""lil_modules.py: A collection of functions."""


__author__ = "Lily Konadu Gyammerah"
__email__ = "lk.gyammerah@st.hanze.nl"
__version__ = "0.0.1"
__license__ = "CC-BY-SA-4.0"


# import modules

import pandas as pd
import numpy as np
import yaml
import matplotlib.pyplot as plt
import seaborn as sns



# loading and reading data 

def load_excel_from_yaml(yaml_file):
    """
    Load an Excel file based on the file path specified in a YAML configuration file.

    Parameters:
    yaml_file (str): The path to the YAML configuration file.

    Returns:
    pandas.DataFrame: A DataFrame containing the data from the Excel file.
    """
    # Loading the YAML configuration file
    with open(yaml_file, "r") as file:
        config = yaml.safe_load(file)

    # Extracting the Excel file path from the YAML config
    excel_file_path = config['Path']

    # Opening the Excel file using pandas
    df = pd.read_excel(excel_file_path)

    return df


def load_excel_sheet_from_yaml(yaml_file, sheet_name):
    """
    Load a specific sheet from an Excel file based on the file path specified in a YAML configuration file.

    Parameters:
    yaml_file (str): The path to the YAML configuration file.
    sheet_name (str): The name of the sheet to be loaded.

    Returns:
    pandas.DataFrame: A DataFrame containing the data from the specified sheet of the Excel file.
    """
    # Loading the YAML configuration file
    with open(yaml_file, "r") as file:
        config = yaml.safe_load(file)

    #Extracting the Excel file path from the YAML config
    excel_file_path = config['Path']

    #Opening the specified sheet from the Excel file using pandas
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

    return df


# Visualization

def plot_bar(df, x_column, y_column, title):
    """
    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data.
    x_column (str): The column to use for the x-axis.
    y_column (str): The column to use for the y-axis.
    title (str): The title of the plot.
    """
    # Sort the DataFrame by the x_column in descending order
    df_sorted = df.sort_values(by=x_column, ascending=False)

    # Create the bar plot
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_sorted, x=x_column, y=y_column)
    plt.title(title)
    plt.show()






if __name__ == "__main__":
    print(__doc__)
else:
    print(f"Module '{__name__}' is imported successfully!\n")
    

