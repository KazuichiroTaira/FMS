import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import datetime
import seaborn as sns


DATA_FOLDER = 'data'
FIG_FOLDER = 'fig'

os.makedirs(FIG_FOLDER, exist_ok=True)

data_file = os.path.join(DATA_FOLDER, 'stageinfamilycycle.csv')
df = pd.read_csv(data_file, sep=";", index_col=[0])

#print(df.head())

df = df.melt()
print(df.head())

row_list = []
for i, row in df.iterrows():
    # Extract gender and year from label
    _, _, _, gender, year = row["variable"].split(" ")

    # Convert ugly string into a number of minutes
    str_value = str(row["value"])
    h, m = str_value.split(".")
    time = int(h) * 60 + int(m)

    # Add new row to the list (as a dictionary)
    row_list.append(
        {"year": year, "gender": gender, "time (in minutes)": time}
    )

# Create new dataframe

clean_df = pd.DataFrame(row_list)
clean_df.to_csv(os.path.join(DATA_FOLDER, "clean_stageinfamilycycle.csv"), index=False)

df = pd.read_csv(os.path.join(DATA_FOLDER, "clean_stageinfamilycycle.csv.csv"))

sns.lineplot(data=df, x="year", y="time (in minutes)", hue="gender")
plt.show()
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

DATA_FOLDER = 'data'
FIG_FOLDER = 'fig'

os.makedirs(FIG_FOLDER, exist_ok=True)

data_file = os.path.join(DATA_FOLDER, 'stageinfamilycycle.csv')
df = pd.read_csv(data_file, sep=";", index_col=[0])
