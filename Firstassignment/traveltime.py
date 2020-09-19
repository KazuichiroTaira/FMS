import matplotlib.pyplot as plt
import pandas as pd
import os
import seaborn as sns

DATA_FOLDER = 'data'
FIG_FOLDER = 'fig'

os.makedirs(FIG_FOLDER, exist_ok=True)

data_file = os.path.join(DATA_FOLDER, 'traveltime.csv')
df = pd.read_csv(data_file, sep=";", index_col=[0])

# Flip the dataframe
df = df.melt()

# Create clean dataframe --------------------------

# Extract data
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

# Create the new dataframe
clean_df = pd.DataFrame(row_list)
clean_df.to_csv(os.path.join(DATA_FOLDER, "clean_traveltime.csv"), index=False)

df = pd.read_csv(os.path.join(DATA_FOLDER, "clean_traveltime.csv"))
sns.lineplot(data=df, x="year", y="time (in minutes)", hue="gender")
plt.savefig(os.path.join(FIG_FOLDER, "traveltime.png"), dpi=300)