# rl_quant_study

A reinforcement learning framework for quantitative trading research and experimentation.

## Project Structure

The main project is organized in the `rl-quant/` directory:

```
rl-quant/
├── data/          # Raw + processed market data
├── envs/          # Custom gym environments
├── models/        # NN / policy definitions
├── experiments/   # Run configs, seeds
├── logs/          # Metrics, tensorboard, csv
├── notebooks/     # Analysis only (no core logic)
├── scripts/       # Training / backtest entrypoints
└── README.md
```

For detailed documentation, see [rl-quant/README.md](rl-quant/README.md).