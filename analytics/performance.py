def evaluate_performance(returns):
    cumulative = (1 + returns).cumprod()
    total_return = cumulative.iloc[-1] - 1
    annualized = (1 + total_return) ** (252 / len(returns)) - 1
    sharpe_ratio = returns.mean() / returns.std() * (252 ** 0.5)
    return {
        "Total Return": f"{total_return:.2%}",
        "Annualized Return": f"{annualized:.2%}",
        "Sharpe Ratio": f"{sharpe_ratio:.2f}"
    }
