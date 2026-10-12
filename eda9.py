import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs('results', exist_ok=True)

# Data load
df = pd.read_csv('results/trades_clean.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
df = df.sort_values('timestamp').dropna(subset=['timestamp', 'price'])

# Rolling average - 30 day ya 100 trades
df['rolling_avg'] = df['price'].rolling(window=100, min_periods=1).mean()

print("--- EDA9 OUTPUT ---")
print(f"Total Trades: {len(df)}")
print(f"Peak Price: {df['price'].max()}")
print(f"Average Price: {df['price'].mean():.2f}")

# Graph 1 - Final Summary
plt.figure(figsize=(12, 6))
plt.plot(df['timestamp'], df['price'], color='#7ec4ff', label='BTC Price', linewidth=1)
plt.plot(df['timestamp'], df['rolling_avg'], color='#ff6b6b', label='30-Day Rolling Average', linewidth=2)
plt.title('EDA9 - BTC Price Trend Final Summary', fontsize=14, fontweight='bold')
plt.xlabel('Timestamp')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('results/eda9.png', dpi=300)
print("Saved: results/eda9.png")

plt.close()
print("Done! Graph ban gaya.")