# Sequencing analysis

## Functionality
The 'dsph.py' module is designed to generate barbell plots that visualize comparative results from sequencing output results as collected in KrakEN or Bracken summary files. The module functions coherently with configuration from a YAML file where the user specifies *two* summary files (with correct path).

Optionally, the user specifies microbial species to solely use for comparing, and/or a top n species to show in the results. Results are generated as a graph that visualizes the changes in species proportions before and after a certain event.

## Notes
> If the 'before' and 'after' KraKEN summary files do not contain the same species (or have a name difference), a comparison cannot be made.
> This module does *not* yet differentiate the different taxonomic levels. That means that this module currently works best when the user already has a selection of species in mind that should be used for comparison.

## Requirements
    - yaml
    - pandas, matplotlib

If desired, all requirements can be installed via:
> `pip install -r requirements.txt`

## Usage of module
### Configuration
1. Add filepath + file to KrakEN/Bracken summary file from measurement A (required)
2. Add filepath + file to KrakEN/Bracken summary file from measurement B (required)
3. Optional: add list of species to solely include in analysis (default = 20)
4. Optional: specify the top 'n' species to solely show in graph (based on largest relative proportions) (default = no selection)

*Note*: for example usage, the configuration file is currently linked to a file path that refers to example data files that were used to develop this module. This data is property of Hanze University Groningen, Institute for Life Science and Technology, Groningen, The Netherlands. All rights belong to them.

###
As soon as the configuration file is correct and not changed in name, the main python module is automatically compatible with the configuration file and can be run like:

'''{python}
./dsph.py
'''

or

'''{python}
python dsph.py
'''

The default interpreter is python3.

## Example usage
For example usage, the config.yaml and dsph.py file are ready for usage. As long as all dependencies (yaml, pandas, matplotlib) are installed, the main module can be run as described above.
