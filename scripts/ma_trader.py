import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------- config ----------
DATA_PATH = "data/btc_usdt_1h.csv"
INITIAL_CASH = 10_000.0
FEE_RATE = 0.001

SHORT_WINDOW = 24
LONG_WINDOW = 240
# ----------------------------

df = pd.read_csv(DATA_PATH, parse_dates=["timestamp"])

# Compute moving averages
df["ma_short"] = df["close"].rolling(window=SHORT_WINDOW).mean()
df["ma_long"] = df["close"].rolling(window=LONG_WINDOW).mean()

cash = INITIAL_CASH
btc = 0.0
equity_curve = []

for i in range(len(df)):
    price = df.loc[i, "close"]
    ma_s = df.loc[i, "ma_short"]
    ma_l = df.loc[i, "ma_long"]

    # Skip until both MAs exist
    if pd.isna(ma_s) or pd.isna(ma_l):
        equity_curve.append(cash + btc * price)
        continue

    # BUY signal
    if ma_s < ma_l and cash > 0:
        btc = (cash / price) * (1 - FEE_RATE)
        cash = 0.0

    # SELL signal
    elif ma_s > ma_l and btc > 0:
        cash = (btc * price) * (1 - FEE_RATE)
        btc = 0.0

    equity = cash + btc * price
    equity_curve.append(equity)

# ---------- results ----------
final_equity = equity_curve[-1]
ret = (final_equity / INITIAL_CASH - 1) * 100

print(f"Final equity: {final_equity:.2f} USDT")
print(f"Return: {ret:.2f}%")

pd.DataFrame({"equity": equity_curve}).to_csv(
    "logs/ma_equity.csv", index=False
)

# ---------- plot ----------
os.makedirs("plots", exist_ok=True)

plt.figure(figsize=(12, 5))
plt.plot(equity_curve, label="MA Strategy")
plt.axhline(INITIAL_CASH, linestyle="--", color="gray", label="Initial Cash")
plt.legend()
plt.title("Moving Average Crossover Equity Curve")
plt.xlabel("Time step")
plt.ylabel("Equity (USDT)")
plt.tight_layout()
plt.savefig("plots/ma_equity.png")

print("Saved plot to plots/ma_equity.png")
