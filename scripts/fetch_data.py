import ccxt
import pandas as pd
from datetime import datetime, timedelta

exchange = ccxt.binance()

symbol = 'BTC/USDT'
timeframe = '1h'
limit = 1000

ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)

df = pd.DataFrame(
    ohlcv, 
    columns=['timestamp', 'open', 'high', 'low', 'close', 'volume']
)

df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
output_path = "data/btc_usdt_1h.csv"
df.to_csv(output_path, index=False)

print(f"Saved {len(df)} rows to {output_path}")
print(df.tail())