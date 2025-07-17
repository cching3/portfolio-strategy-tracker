from analytics.performance import evaluate_performance
from data.fetch import fetch_timeseries

class BacktestRunner:
    @staticmethod
    def run(strategy, tickers, start_date, end_date):
        outcome = {}
        for symbol in tickers:
            prices = fetch_timeseries(symbol, start_date, end_date)
            signals = strategy(prices)
            returns = (signals.shift(1) * prices.pct_change()).fillna(0)
            metrics = evaluate_performance(returns)
            outcome[symbol] = metrics
        return outcome