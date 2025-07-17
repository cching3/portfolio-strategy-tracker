import yfinance as yf


def fetch_timeseries(symbol, start_date, end_date):
    try:
        data = yf.download(symbol, start=start_date, end=end_date, progress=False)
        if len(data) > 0 and "Adj Close" in data.columns:
            return data["Adj Close"]
        else:
            import pandas as pd
            import numpy as np
            # Return empty series with NaN values if no data is available
            return pd.Series(np.nan, index=pd.date_range(start=start_date, end=end_date))
    except Exception as e:
        import pandas as pd
        import numpy as np
        print(f"Error fetching data for {symbol}: {e}")
        # Return empty series with NaN values if API call fails
        return pd.Series(np.nan, index=pd.date_range(start=start_date, end=end_date))


def fetch_price(symbol):
    data = yf.Ticker(symbol).history(period="1d")
    if len(data) > 0 and "Close" in data.columns:
        return data["Close"].iloc[-1]
    else:
        # If no data is available, try getting the last available quote
        try:
            ticker_info = yf.Ticker(symbol).info
            if "previousClose" in ticker_info:
                return ticker_info["previousClose"]
            elif "regularMarketPrice" in ticker_info:
                return ticker_info["regularMarketPrice"]
            else:
                return 0.0  # Return 0 if no price data is available
        except:
            return 0.0  # Return 0 if API call fails
