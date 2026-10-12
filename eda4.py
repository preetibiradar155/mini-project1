import pandas as pd
df = pd.read_csv('trades.csv')
df = df.drop_duplicates(subset=['trade_id'])
df['side'] = df['side'].astype(str).str.upper().str.strip()
df['symbol'] = df['symbol'].astype(str).str.upper().str.strip()
df['price'] = pd.to_numeric(df['price'].astype(str).str.replace(',',''), errors='coerce')
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce', utc=True)
df = df.dropna(subset=['price','timestamp'])
df = df[df['price']>0]
df.to_csv('results/trades_clean.csv', index=False)
print(f"Saved results/trades_clean.csv Shape: {df.shape}")