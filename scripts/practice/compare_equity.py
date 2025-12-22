import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("plots", exist_ok=True)

random_eq = pd.read_csv("logs/random_equity.csv")["equity"]
ma_eq = pd.read_csv("logs/ma_equity.csv")["equity"]

plt.figure(figsize=(12, 5))
plt.plot(random_eq, label="Random Trader", alpha=0.7)
plt.plot(ma_eq, label="MA Strategy", alpha=0.9)

plt.axhline(10_000, linestyle="--", color="gray", label="Initial Cash")
plt.title("Equity Curve Comparison")
plt.xlabel("Time step")
plt.ylabel("Equity (USDT)")
plt.legend()
plt.tight_layout()
plt.savefig("plots/compare_equity.png")

print("Saved plot to plots/compare_equity.png")
