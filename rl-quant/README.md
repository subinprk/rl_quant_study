# RL Quant Study

A reinforcement learning framework for quantitative trading research and experimentation.

## Project Structure

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

## Directory Descriptions

### `data/`
Contains raw and processed market data used for training and backtesting.
- Raw market data (price, volume, tick data)
- Processed/cleaned datasets
- Feature-engineered data

### `envs/`
Custom OpenAI Gym environments for trading simulations.
- Trading environment implementations
- State/action space definitions
- Reward function implementations

### `models/`
Neural network architectures and RL policy definitions.
- Policy networks (Actor)
- Value networks (Critic)
- Custom architectures (CNN, LSTM, Transformer)

### `experiments/`
Experiment configurations and hyperparameters.
- YAML/JSON configuration files
- Hyperparameter settings
- Random seeds for reproducibility

### `logs/`
Training outputs, metrics, and model checkpoints.
- TensorBoard event files
- Training metrics and loss curves
- CSV exports
- Model checkpoints

### `notebooks/`
Jupyter notebooks for analysis and visualization.
- Data exploration
- Results analysis
- Performance visualization
- **Note:** No core logic should be in notebooks

### `scripts/`
Entry point scripts for training and evaluation.
- Training scripts
- Backtesting scripts
- Data preprocessing
- Evaluation and testing

## Getting Started

1. Set up your environment:
   ```bash
   pip install -r requirements.txt  # (when available)
   ```

2. Prepare your data in `data/`

3. Define or use existing environments from `envs/`

4. Configure your experiment in `experiments/`

5. Run training scripts from `scripts/`

6. Analyze results using notebooks in `notebooks/`

## Development Guidelines

- Keep core logic in proper modules (`envs/`, `models/`, `scripts/`)
- Use notebooks only for analysis and visualization
- Document all experiments and configurations
- Version control experiment configurations
- Use meaningful names for files and experiments

## License

[Add your license here]

## Contributors

[Add contributors here]
