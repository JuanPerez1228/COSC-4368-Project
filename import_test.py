import pandas as pd

# Replace 'your_dataset.csv' with your actual dataset filename
df = pd.read_csv('your_dataset.csv')
print(df.head())
print(df.info())
print(df.describe())
