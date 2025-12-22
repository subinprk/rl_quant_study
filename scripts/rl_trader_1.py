import gymnasium as gym
from gymnasium import spaces

class TradingEnv(gym.Env):
	def __init__(self, df, initial_balance=10000):
		super(TradingEnv, self).__init__()

		self.df = df
		self.initial_balance = initial_balance
		self.current_step = 0

		# action space : for now only 2 options
		# 0 for look or sell
		# 1 for buy or hold
		self.action_space = spaces.Discrete(2)

		# Observation Space: [RSI, Volatility, Log Return,Position_Hold]
		self.observation_space = spaces.Box(
			low = -np.inf, 
		)
