import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import prepare_features

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

# Max Drawdown (MDD)
df['peak'] =df['strategy_wealth'].cummax()
df['drawdown'] = (df['strategy_wealth'] - df['peak']) / df['peak']
max_drawdown = df['drawdown'].min()

# Sharpe Ratio Calculator
df['strat_multiplier'] = (1 + df['strategy_return']) * (1 - FEE_RATE * df['is_trade'])
hourly_returns = df['strat_multiplier'] - 1
sharpe_ratio = np.sqrt(24 * 365) * (hourly_returns.mean() / hourly_returns.std())

#---------- results ----------
print(f"Final equity: {df['buy_hold_wealth'].iloc[-1]:.2f} USDT")
print(f"Return: {df['strategy_wealth'].iloc[-1]:.2f} USDT")
print(f"Max Drawdown: {max_drawdown*100:.2f}%")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")

#--------- visualize -----------
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True, gridspec_kw={'height_ratios': [3, 1]})

ax1.plot(df['timestamp'], df['buy_hold_wealth'], label='Buy & Hold', color='blue', alpha=0.7)
ax1.plot(df['timestamp'], df['strategy_wealth'], label="MA Strategy", color='orange')
ax1.set_ylabel('Equity (USDT)')
ax1.legend()
ax1.set_title('Strategy vs Benchmark Equity Curve')

ax2.fill_between(df['timestamp'], df['drawdown'], 0, color='red', alpha=0.5)
ax2.set_ylabel('Drawdown')
ax2.set_title('Drawdown Over Time')

plt.tight_layout()
plt.show()