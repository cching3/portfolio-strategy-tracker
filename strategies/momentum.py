def momentum_strategy(prices, short_window=20, long_window=50):
    short_avg = prices.rolling(window=short_window).mean()
    long_avg = prices.rolling(window=long_window).mean()
    signal = (short_avg > long_avg).astype(int)
    return signal