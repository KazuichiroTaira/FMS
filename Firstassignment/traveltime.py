import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

DATA_FOLDER = 'data'
FIG_FOLDER = 'fig'

os.makedirs(FIG_FOLDER, exist_ok=True)

data_file = os.path.join(DATA_FOLDER, 'traveltime.csv')
df = pd.read_csv(data_file, sep=";", index_col=[0])

print(df.melt())