import pandas as pd
df = pd.read_csv('trades.csv')
print("Missing:\n", df.isnull().sum())
print("\nDuplicate trade_id:", df.duplicated(subset=['trade_id']).sum())
print("\nDuplicated rows:", df.duplicated().sum())