"""
Data Collector Module
Fetches stock market data from Yahoo Finance
"""

import yfinance as yf
import pandas as pd
from datetime import datetime

def fetch_stock_data(symbol, period="1mo"):
    """
    Fetch historical stock data for a given symbol
    
    Parameters:
    - symbol: Stock ticker (e.g., 'AAPL', 'MSFT')
    - period: Time period (e.g., '1mo', '3mo', '1y')
    
    Returns:
    - DataFrame with stock data
    """
    print(f"Fetching data for {symbol}...")
    
    # Download data from Yahoo Finance
    stock = yf.Ticker(symbol)
    data = stock.history(period=period)
    
    print(f"Retrieved {len(data)} days of data")
    return data

# Test the function
if __name__ == "__main__":
    # Fetch Apple stock data for the last month
    aapl_data = fetch_stock_data("AAPL", period="1mo")
    
    print("\n--- First 5 rows ---")
    print(aapl_data.head())
    
    print("\n--- Data Info ---")
    print(aapl_data.info())
