import streamlit as st
from portfolio.portfolio import PortfolioManager
from portfolio.backtest import BacktestRunner
from strategies.momentum import momentum_strategy
from strategies.mean_reversion import mean_reversion_strategy

st.title("📊 Backfolio: Live Portfolio & Strategy Simulator")

# Example holdings input
example_holdings = {
    "AAPL": {"shares": 15, "entry_price": 145, "entry_date": "2023-01-10"},
    "GOOG": {"shares": 8, "entry_price": 2800, "entry_date": "2023-03-15"}
}

portfolio = PortfolioManager(example_holdings)
st.subheader("Live Portfolio Overview")
st.write(f"📈 Current Portfolio Value: ${portfolio.calculate_value():,.2f}")

st.subheader("🔁 Run Strategy Backtest")
asset_list = ["AAPL", "GOOG"]

# Create a strategy selector
strategy_option = st.selectbox(
    "Select Strategy",
    ["Momentum", "Mean Reversion"]
)

# Run the selected strategy
if strategy_option == "Momentum":
    results = BacktestRunner.run(
        strategy=momentum_strategy,
        tickers=asset_list,
        start_date="2020-01-01",
        end_date="2024-01-01"
    )
    st.write("Momentum Strategy Results:")
else:
    results = BacktestRunner.run(
        strategy=mean_reversion_strategy,
        tickers=asset_list,
        start_date="2020-01-01",
        end_date="2024-01-01"
    )
    st.write("Mean Reversion Strategy Results:")

st.write(results)