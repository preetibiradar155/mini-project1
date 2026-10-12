import pandas as pd
import os
os.makedirs('results', exist_ok=True)
df = pd.read_csv('trades.csv')
print("--- head() ---")
print(df.head())
print("\n--- shape ---", df.shape)
print("\n--- info() ---")
print(df.info())
print("\n--- dtypes ---\n", df.dtypes)
# Save for GitHub
with open('results/RESULTS.md','w', encoding='utf-8') as f:
    f.write(f"# Step1 Load\nShape: {df.shape}\nColumns: {df.columns.tolist()}\n\n{df.head().to_string()}\n")
    
    