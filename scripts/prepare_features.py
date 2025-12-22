import numpy as np

def prepare_features(df):
	df['log_return'] = np.log(df['close'] / df['close'].shift(1))

	# volatility--standart derivation of 24 hrs of log returns
	df['volatility'] = df['log_return'].rolling(window=24).std()
	
	# RSI
	delta = df['close'].diff()
	gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
	loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
	rs = gain / loss
	df['rsi'] = 100 - (100 / (1 + rs))

	return df.dropna()