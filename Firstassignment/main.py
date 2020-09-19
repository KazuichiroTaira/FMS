import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

DATA_FOLDER = 'data'
FIG_FOLDER = 'fig'

os.makedirs(FIG_FOLDER, exist_ok=True)

data_file = os.path.join(DATA_FOLDER, 'data.csv')
df = pd.read_csv(data_file, sep=";", index_col=[0])

print(df.head())
# print(df.index)

print(df.columns)

print(df.loc['01-26  Total'].astype("float") )

# c_list = ['Participated, % Women 2009', 'Time used hours,minutes Total 1979']

for c_name in df.columns:
    try:
        df[c_name] = df[c_name].astype('float')
    except ValueError:
        print(f'got troubles with {c_name}')
# print(df["Time used hours,minutes Total 1979"])
