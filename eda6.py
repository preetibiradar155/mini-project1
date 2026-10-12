import pandas as pd
import os

# file ka sahi path
path = 'results/trades_clean.csv' if os.path.exists('results/trades_clean.csv') else 'trades.csv'
df = pd.read_csv(path)

print("File loaded:", path)
print(df.head())

# timestamp ko sahi karo
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
# price ko number me badlo
df['price'] = pd.to_numeric(df['price'], errors='coerce')

print("\nData Types:")
print(df.dtypes)

print("\nTimestamp sample:")
print(df['timestamp'].head())

# clean file ko wapas save karo
df.to_csv('results/trades_clean.csv', index=False)
print("\nSaved to results/trades_clean.csv")