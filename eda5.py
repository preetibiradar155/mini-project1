import pandas as pd
df = pd.read_csv('results/trades_clean.csv')
print(df.describe())
print("\nSide counts:\n", df['side'].value_counts())