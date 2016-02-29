import pandas as pd
import h5py

def hdf5_to_dataframe(filename):
    hdf5_file = h5py.File(filename, 'r')

    dataset = list(hdf5_file.keys())[0]
    hdf5_file.close()

    df = pd.read_hdf(filename, key=dataset)
    return df

def get_row_count(df):
    return len(df.index)