import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

DATA_FOLDER = 'data'
FIG_FOLDER = 'fig'

os.makedirs(FIG_FOLDER, exist_ok=True)

data_file = os.path.join(DATA_FOLDER, 'stageinfamilycycle.csv')
df = pd.read_csv(data_file, sep=";", index_col=[0])
