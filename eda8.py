import pandas as pd
df = pd.read_csv('results/trades_clean.csv')
print("--- EDA7 OUTPUT ---")
df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df.sort_values('timestamp')
print(df[['timestamp','price']].tail(10))
print("\nLast 5 trades price change:")
print(df['price'].diff().tail())