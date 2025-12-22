import pandas as pd
import numpy as np

#---------- config ----------
DATA_PATH = "data/btc_usdt_1h.csv"
INITIAL_CASH = 10_000.0
FEE_RATE = 0.001
SHORT_WINDOW = 24
LONG_WINDOW = 240
#---------------------------
df = pd.read_csv(DATA_PATH, parse_dates=["timestamp"])

df["ma_short"] = df["close"].rolling(window=SHORT_WINDOW).mean()
df["ma_long"] = df["close"].rolling(window=LONG_WINDOW).mean()

cash = INITIAL_CASH
btc = 0.0
equity_curve = []

df["signal"] = 0.0
#buy condition
df.loc[df['ma_short'] < df["ma_long"], 'signal'] = 1.0

df['market_return'] = df['close'].pct_change()
df['strategy_return'] = df['signal'].shift(1) * df['market_return']

df['buy_hold_wealth'] = INITIAL_CASH * (1 + df['market_return']).cumprod()
df['strategy_wealth'] = INITIAL_CASH * ((1 + df['strategy_return'])*(1 - FEE_RATE * df['signal'].diff().abs())).cumprod()

#calculate strategy returns (before fees)
df['strat_ret_gross'] = df['signal'].shift(1) * df['market_return']
#Identify trades: 1 if we bought or sold, 0 if we held
df['is_trade'] = df['signal'].diff().abs().fillna(0)

strategy_wealth = [INITIAL_CASH]
for i in range(1, len(df)):
	new_wealth = strategy_wealth[-1] * (1 + df['strat_ret_gross'].iloc[i])
	if df['is_trade'].iloc[i] == 1:
		new_wealth -= new_wealth * FEE_RATE
	strategy_wealth.append(new_wealth)
	
print(f"Final equity: {df['buy_hold_wealth'].iloc[-1]:.2f} USDT")
print(f"Return: {df['strategy_wealth'].iloc[-1]:.2f} USDT")