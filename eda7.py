import pandas as pd
df = pd.read_csv('results/trades_clean.csv')
print("--- EDA6 OUTPUT ---")
print("Total Trades:", len(df))
print("Price Mean:", df['price'].mean())
print("Price Max:", df['price'].max())
print("Price Min:", df['price'].min())