import numpy as np
import pandas as pd

def load_and_describe_data(csv_file_path_name):
    """Function to load data into a Pandas DataFrame and
       describe the data"""
    df = pd.read_csv(csv_file_path_name)
    df.columns = [col_name.lower() for col_name in df.columns]
    print('*'*10)
    print(df.info())
    print('*'*10)
    print(df.columns)
    print('*'*10)
    print(df.duplicated().sum())
    print('*'*10)
    print(df.isnull().sum())
    print('*'*10)
    print(df.describe())
    return df