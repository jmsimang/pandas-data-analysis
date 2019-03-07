"""
Import flat files with NumPy
"""


"""
Import flat files with Pandas DataFrame and applying iteration and slicing,
using 'read_csv()':
    nrows=, header=, sep=, comment=, na_values= (as arguments)
"""
import pandas as pd

def load_csv(filename):
    return pd.read_csv(filename)

csv_df = load_csv('./data_files/supermarkets.csv')


"""
Import Excel, MATLAB, SAS, HDF5, Stata, and Pickled files using pandas
[Pickled - a file that has been converted into bytestream, i.e, Serialized
"""
# Pickled files
import pickle

def load_pickle(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

unpickled = load_pickle('./data_files/supermarkets.json')
print(type(unpickled))
print(unpickled)

# Excel files
def load_xls(filename):
    file = pd.ExcelFile(filename)
    print('Done. File has sheet names: ', file.sheet_names)
    ui = input('Do you want to continue and enter a sheet name? Y or N: ')
    if ui.lower() == 'y':
        sheet = input('Please enter sheet name, or an index (from zero): ')
        if sheet in file.sheet_names:
            print('Retrieving only sheet {}'.format(sheet))
            return parse_xls_sheet(file, sheet)
            # Additional arguments to parse function
            # return file.parse(file, parse_cols=, skiprows=, names=)
        else:
            print('Invalid sheet name or index. Please try again.')
    elif ui.lower() == 'n':
        print('Returning serialized file as is')
        return file
    else:
        print('Invalid entry. Please try again.')

def parse_xls_sheet(file, sheet):
    # Additional arguments to skip rows and rename columns - as lists or not
    # return file.parse(sheet, skiprows=, names=)
    return file.parse(sheet)

xls_df = load_xls('./data_files/supermarkets.xlsx')
print(type(xls_df))
print(xls_df)


# SAS/Stata files
