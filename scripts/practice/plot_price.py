import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("plots", exist_ok=True)

df = pd.read_csv("data/btc_usdt_1h.csv", parse_dates=["timestamp"])
plt.figure(figsize=(12, 5))
plt.plot(df["timestamp"], df["close"])
plt.title("BTC/USDT Closing Prices (1h)")
plt.xlabel("Time")
plt.ylabel("Price (USDT)")
plt.tight_layout()
plt.savefig("plots/btc_price.png")