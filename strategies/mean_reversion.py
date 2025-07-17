def mean_reversion_strategy(prices, window=20):
    rolling_mean = prices.rolling(window=window).mean()
    rolling_std = prices.rolling(window=window).std()
    z_score = (prices - rolling_mean) / rolling_std
    # Buy when price is below 2 standard deviations
    # Sell when price is above 2 standard deviations
    return (z_score < -2).astype(int) - (z_score > 2).astype(int)