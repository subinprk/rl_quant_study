import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

#--------------config--------------
DATA_PATH = "./data/btc_usdt_1h.csv"
INITIAL_CASH = 10_000.0
FEE_RATE = 0.001

SHORT_WINDOW = 10
LONG_WINDOW = 50
#----------------------------------
df = pd.read_csv(DATA_PATH, parse_dates=["timestamp"])

# Compute moving averages
df["ma_short"] = df["close"].rolling(window=SHORT_WINDOW).mean()
df["ma_long"] = df["close"].rolling(window=LONG_WINDOW).mean()

cash = INITIAL_CASH
btc = 0.0
equity_curve = []

for i in range(len(df)):
    price = df.loc[i, "close"]

    action = np.random.choice([0,1,2]) #hold, buy, sell

    # BUY
    if action == 1 and cash > 0:
        btc = (cash / price) * (1 - FEE_RATE)
        cash = 0.0
    # SELL
    elif action == 2 and btc > 0:
        cash = (btc * price) * (1 - FEE_RATE)
        btc = 0.0

    equity = cash + btc * price
    equity_curve.append(equity)

#-----------results----------------
final_equity = equity_curve[-1]
print(f"Final equity: {final_equity:.2f} USDT")
print(f"Return: {(final_equity/ INITIAL_CASH - 1) * 100:.2f}%")
pd.DataFrame({"equity": equity_curve}).to_csv(
    "logs/random_equity.csv", index=False
)

#-------------plot-----------------
os.makedirs("plots", exist_ok=True)

plt.figure(figsize=(12, 5))
plt.plot(equity_curve)
plt.title("Random Trader Equity Curve")
plt.xlabel("Time step")
plt.ylabel("equity (USDT)")
plt.tight_layout()
plt.savefig("plots/random_equity.png")

print("Saved plot to plots/random_equity.png")