#!/usr/bin/env python3

"""
Kraken Dual Output Comparison Tool
----------------------------------
This module is designed to generate barbell plots that
visualize comparative results from sequencing output
results as collected in KraKEN summary files. The module
functions coherently with configuration from a YAML file
where the user specifies *two* KraKEN summary files (with
correct path).

Optionally, the user specifies microbial species to solely
use for comparing, and/or a top n species to show in the
results. Results are generated as a graph that visualizes
the changes in species proportions before and after a
certain event.

Note:
If the 'before' and 'after' KraKEN summary files do not
contain the same species (or have a name difference),
a comparison cannot be made.

Note:
This module does *not* yet differentiate the different
taxonomic levels. That means that this module currently
works best when the user already has a selection of
species in mind that should be used for comparison.

Requirements:
    - yaml
    - pandas, matplotlib

If desired, all requirements can be installed via:
    pip install -r requirements.txt
"""

import yaml
import pandas as pd
import matplotlib.pyplot as plt

#################
#  load config  #
#################
def load_config(config_filename='config.yaml'):
    """
    Loads configuration settings from a YAML file.

    Parameters:
    - config_filename: str, optional (default name 'config.yaml')
        The name of the YAML configuration file to load.

    Returns:
    - configuration: dict
        The loaded configuration settings as a dictionary.
    """
    with open(config_filename, 'r', encoding='utf-8') as file:
        configuration = yaml.safe_load(file)
    return configuration

#################
#   read data   #
#################
def read_data(file_path, selection=None, top_n=None):
    """
    Reads data from a given file path and optionally filters
    by selected species and/or retrieves the top n results
    based on highest percentage and thus strongest occurrence.

    Parameters:
    - file_path: str
        The path to the data file to read.
    - selection: list, optional
        A list of species to filter the data by.
    - top_n: int, optional
        The number of top results to retrieve (based on %).

    Returns:
    - filtered_data: DataFrame
        A pandas DataFrame containing the filtered data.
    """
    data_frame = pd.read_csv(file_path, sep='\t', header=None, encoding='utf-8',
                             # add column names to KraKEN output data
                             names=['Percentage', 'Reads', 'Reads_Children',
                                    'Rank', 'TaxID', 'Taxon'],
                             # only 'Percentage' and 'Taxon' are loaded
                             usecols=['Percentage', 'Taxon'])

    # stripping all possible whitespace from Taxon column
    data_frame['Taxon'] = data_frame['Taxon'].str.strip()

    # converting all percentages to a numeric type
    # errors='coerce' specifies that if conversion is
    # not possible (e.g. if the data contains 'N/A'),
    # that non-convertable data should be replaced with NaN
    data_frame['Percentage'] = pd.to_numeric(data_frame['Percentage'],
                                             errors='coerce')

    ### DEAL WITH OPTIONAL CONFIGURATION ###
    if selection: # if specified, only store selected species in df
        data_frame = data_frame[data_frame['Taxon'].isin(selection)]

    if top_n: # if specified, only store 'n' largest results in df
        data_frame = data_frame.nlargest(top_n, 'Percentage')

    return data_frame

#################
# generate plot #
# main function #
#################
if __name__ == '__main__':

    ### LOAD CONFIGURATION ###
    config = load_config()

    before_file_path = config['kraken_files']['before_measurement_file']
    after_file_path = config['kraken_files']['after_measurement_file']
    selected_species = config.get('selected_species', []) # default = empty list
    top_n_species = config.get('top_n_species', None) # default = None

    ### READ & PROCESS DATA ###
    data_before = read_data(before_file_path, selected_species, top_n_species)
    data_after = read_data(after_file_path, selected_species, top_n_species)

    # combine before and after data, exclude the unclassified for plotting
    combined_data = pd.merge(data_before[data_before['Taxon'] != 'unclassified'],
                             data_after[data_after['Taxon'] != 'unclassified'],
                             on='Taxon', suffixes=('_before', '_after'))

    ### PLOTTING ###
    # specify plot style and size
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(14, 8))

    # add horizontal lines in graph for connecting scatter points
    ax.hlines(combined_data.index, combined_data['Percentage_before'],
              combined_data['Percentage_after'], color='black', alpha=0.4,
              linewidth=2)

    # scatter points for before measurements
    ax.scatter(combined_data['Percentage_before'], combined_data.index,
               color='teal', alpha=1, s=120, linewidth=0.6, edgecolor='black',
               label='Before Measurement', zorder=5)

    # scatter points for after measurements
    ax.scatter(combined_data['Percentage_after'], combined_data.index,
               color='coral', alpha=0.8, s=120, linewidth=0.6, edgecolor='black',
               label='After Measurement', zorder=5)

    # add labels and titles
    ax.set_ylabel('Taxon', fontsize=16, fontweight='light', color='gray')
    ax.set_xlabel('Percentage (%)', fontsize=16, fontweight='light', color='gray')
    ax.set_title('Species Proportions Before vs. After', fontsize=20,
                 fontweight='bold', color='gray', pad=20)

    # add ticks and tick labels
    ax.tick_params(axis='y', labelsize=12, labelcolor='gray')
    ax.tick_params(axis='x', labelsize=12, labelcolor='gray')
    ax.set_yticks(range(len(combined_data['Taxon'])))
    ax.set_yticklabels(combined_data['Taxon'], fontsize=12, fontweight='light')

    # add and place legend
    ax.legend(frameon=False, fontsize=12, loc='upper left',
              bbox_to_anchor=(1, 1))

    # edit graph axis spines (color)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('lightgray')
    ax.spines['bottom'].set_color('lightgray')

    # adjust position of graph in output window
    plt.subplots_adjust(right=0.8)

    plt.show()
